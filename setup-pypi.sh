#!/bin/bash
# PyPI Setup Script for Smart Clipboard Manager

set -e

echo "🐍 Setting up PyPI publishing for Smart Clipboard Manager..."
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

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

# Check if gh is available
if ! command -v gh &> /dev/null; then
    print_error "GitHub CLI (gh) is not installed. Please install it first."
    echo "Install with: sudo apt install gh"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    print_error "Not authenticated with GitHub. Please run: gh auth login"
    exit 1
fi

print_success "GitHub CLI is authenticated"

# Check repository
REPO_OWNER=$(gh api user --jq '.login')
REPO_NAME="linux-clipboard-manager"

print_info "Repository: $REPO_OWNER/$REPO_NAME"

# Check if package builds successfully
echo ""
print_info "Building package to verify everything works..."
if python3 setup.py sdist bdist_wheel &> /dev/null; then
    print_success "Package builds successfully"
else
    print_error "Package build failed. Please check the setup.py file."
    exit 1
fi

# Check built files
if [ -f "dist/smart_clipboard_manager-1.0.0-py3-none-any.whl" ] && [ -f "dist/smart-clipboard-manager-1.0.0.tar.gz" ]; then
    print_success "Built packages found in dist/"
else
    print_error "Built packages not found in dist/"
    exit 1
fi

echo ""
print_info "Next steps to complete PyPI setup:"
echo ""

echo "1️⃣  Create PyPI account:"
echo "   Go to https://pypi.org/ and register"
echo ""

echo "2️⃣  Generate PyPI API token:"
echo "   - Log in to PyPI"
echo "   - Go to Account Settings → API tokens"
echo "   - Click 'Add API token'"
echo "   - Select 'Entire account' scope"
echo "   - Copy the generated token"
echo ""

echo "3️⃣  Add token to GitHub secrets:"
echo "   Choose one of these methods:"
echo ""

echo "   Method A - Using GitHub CLI (recommended):"
echo "   gh secret set PYPI_API_TOKEN --body \"your-pypi-token-here\""
echo ""

echo "   Method B - Using GitHub web interface:"
echo "   - Go to: https://github.com/$REPO_OWNER/$REPO_NAME/settings/secrets/actions"
echo "   - Click 'New repository secret'"
echo "   - Name: PYPI_API_TOKEN"
echo "   - Value: paste your PyPI token"
echo ""

echo "4️⃣  Test the setup:"
echo "   - Check secrets: gh secret list"
echo "   - Create a test release: gh release create v1.0.1 --title \"Test Release\" --notes \"Testing PyPI publishing\""
echo ""

echo "5️⃣  Verify PyPI publishing:"
echo "   - Check GitHub Actions: https://github.com/$REPO_OWNER/$REPO_NAME/actions"
echo "   - Check PyPI: https://pypi.org/project/smart-clipboard-manager/"
echo ""

print_info "GitHub Actions workflow is already configured!"
print_info "It will automatically test and publish when you create releases."
echo ""

print_success "Setup script completed!"
echo ""
print_warning "Remember to:"
echo "  • Keep your PyPI token secure"
echo "  • Test with a small version increment first"
echo "  • Update changelog in README.md for each release"
echo ""

echo "📚 For detailed instructions, see: PYPI_SETUP.md"
echo "🌐 Your repository: https://github.com/$REPO_OWNER/$REPO_NAME"
echo "📦 GitHub Pages: https://$REPO_OWNER.github.io/$REPO_NAME/"
