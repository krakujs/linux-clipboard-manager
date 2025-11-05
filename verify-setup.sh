#!/bin/bash
# Verification script for Smart Clipboard Manager setup

set -e

echo "🔍 Verifying Smart Clipboard Manager setup..."
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check GitHub CLI
if command -v gh &> /dev/null && gh auth status &> /dev/null; then
    print_success "GitHub CLI authenticated"
else
    print_error "GitHub CLI not available or not authenticated"
fi

# Check repository
REPO_OWNER=$(gh api user --jq '.login' 2>/dev/null || echo "unknown")
REPO_NAME="linux-clipboard-manager"
print_info "Repository: $REPO_OWNER/$REPO_NAME"

# Check if files exist
FILES=(
    "README.md"
    "setup.py"
    "requirements.txt"
    "install-system.sh"
    "LICENSE"
    "CONTRIBUTING.md"
    ".github/workflows/publish.yml"
    ".github/workflows/test.yml"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        print_success "$file exists"
    else
        print_error "$file missing"
    fi
done

# Check package build
echo ""
print_info "Testing package build..."
if python3 setup.py sdist bdist_wheel &> /dev/null; then
    print_success "Package builds successfully"
    
    # Check package files
    if [ -f "dist/smart_clipboard_manager-1.0.0-py3-none-any.whl" ] && [ -f "dist/smart-clipboard-manager-1.0.0.tar.gz" ]; then
        print_success "Built packages found"
        
        # Check package with twine
        if command -v twine &> /dev/null; then
            if twine check dist/* &> /dev/null; then
                print_success "Package passes twine validation"
            else
                print_error "Package fails twine validation"
            fi
        else
            print_warning "Twine not available for package validation"
        fi
    else
        print_error "Built packages not found"
    fi
else
    print_error "Package build failed"
fi

# Check GitHub secrets
echo ""
print_info "Checking GitHub secrets..."
if gh secret list &> /dev/null; then
    if gh secret list | grep -q "PYPI_API_TOKEN"; then
        print_success "PYPI_API_TOKEN secret found"
        print_warning "PyPI publishing is ready!"
    else
        print_warning "PYPI_API_TOKEN secret not found"
        print_info "Run ./setup-pypi-token.sh to set it up"
    fi
else
    print_warning "Cannot check GitHub secrets"
fi

# Check repository links
echo ""
print_info "Repository links:"
echo "🌐 GitHub: https://github.com/$REPO_OWNER/$REPO_NAME"
echo "📦 GitHub Pages: https://$REPO_OWNER.github.io/$REPO_NAME/"
echo "📋 Documentation: https://github.com/$REPO_OWNER/$REPO_NAME/blob/main/README.md"
echo "⚡ Actions: https://github.com/$REPO_OWNER/$REPO_NAME/actions"
echo "🏷️ Releases: https://github.com/$REPO_OWNER/$REPO_NAME/releases"

echo ""
print_info "Installation commands for users:"
echo "🚀 One-click: curl -fsSL https://raw.githubusercontent.com/$REPO_OWNER/$REPO_NAME/main/install-system.sh | bash"
echo "📦 pip: pip install smart-clipboard-manager"
echo "📂 Source: pip install git+https://github.com/$REPO_OWNER/$REPO_NAME.git"

echo ""
print_success "Setup verification completed!"
echo ""
if [ -z "$(gh secret list 2>/dev/null | grep PYPI_API_TOKEN)" ]; then
    print_warning "Next step: Run ./setup-pypi-token.sh to enable PyPI publishing"
else
    print_success "Ready to publish! Create a release with: gh release create v1.0.1 --title 'New Release' --notes 'Release notes'"
fi
