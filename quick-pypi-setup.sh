#!/bin/bash
# Quick PyPI Setup - Run this to set up PyPI publishing

echo "🐍 Quick PyPI Setup for Smart Clipboard Manager"
echo ""

# Check GitHub CLI
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI not found. Install with: sudo apt install gh"
    exit 1
fi

echo "✅ GitHub CLI found"
echo ""

echo "📝 To set up PyPI publishing, run:"
echo "   ./setup-pypi-token.sh"
echo ""

echo "🔐 This script will:"
echo "   1. Prompt for your PyPI API token (hidden input)"
echo "   2. Store it securely as a GitHub secret"
echo "   3. Enable automatic PyPI publishing"
echo ""

echo "📦 After setup, you can publish with:"
echo "   gh release create v1.0.1 --title 'New Release' --notes 'Release notes'"
echo ""

echo "🌐 Repository: https://github.com/krakujs/linux-clipboard-manager"
echo "📦 PyPI (when published): https://pypi.org/project/smart-clipboard-manager/"
