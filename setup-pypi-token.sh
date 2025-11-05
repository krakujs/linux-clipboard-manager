#!/bin/bash
# Secure PyPI Token Setup Script

set -e

echo "🔐 Setting up PyPI token securely..."

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
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
    print_error "GitHub CLI (gh) is not installed."
    exit 1
fi

print_success "GitHub CLI found"

# Check if authenticated
if ! gh auth status &> /dev/null; then
    print_error "Not authenticated with GitHub. Please run: gh auth login"
    exit 1
fi

print_success "GitHub CLI authenticated"

# Get repository info
REPO_OWNER=$(gh api user --jq '.login')
REPO_NAME="linux-clipboard-manager"

print_info "Repository: $REPO_OWNER/$REPO_NAME"

echo ""
print_info "To set up PyPI publishing, you need to:"
echo "1. Have a PyPI API token"
echo "2. Add it as a GitHub secret"
echo ""

# Prompt for the token (hidden input)
print_info "Please enter your PyPI API token:"
echo "(The input will be hidden for security)"
read -s PYPI_TOKEN

if [ -z "$PYPI_TOKEN" ]; then
    print_error "No token provided. Exiting."
    exit 1
fi

echo ""
print_info "Setting PyPI token as GitHub secret..."

# Add the secret to GitHub
if echo "$PYPI_TOKEN" | gh secret set PYPI_API_TOKEN; then
    print_success "PyPI API token set as GitHub secret!"
else
    print_error "Failed to set PyPI token as GitHub secret"
    exit 1
fi

# Clear the token from memory
unset PYPI_TOKEN

echo ""
print_success "PyPI setup completed!"
print_info "The token is now stored securely as a GitHub secret."
print_info "GitHub Actions will use it to publish to PyPI automatically."
echo ""

print_info "Next steps:"
echo "1. Test by creating a new release: gh release create v1.0.1 --title 'Test Release' --notes 'Testing PyPI publishing'"
echo "2. Check the Actions tab on GitHub to see the publishing process"
echo "3. Verify the package appears on PyPI: https://pypi.org/project/smart-clipboard-manager/"
echo ""

print_warning "Important security notes:"
echo "• The token is stored securely in GitHub Secrets"
echo "• It will not be exposed in logs or code"
echo "• Only GitHub Actions can access it"
echo "• You can rotate the token anytime from PyPI"
