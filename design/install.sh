#!/usr/bin/env bash
# Install design skills adapters to a target project directory.
#
# Usage:
#   ./install.sh <target-dir>                    # Install all platforms
#   ./install.sh <target-dir> claude-code        # Install only claude-code
#   ./install.sh <target-dir> codex gemini       # Install codex + gemini
#
# What it does per platform:
#   claude-code   → <target>/.claude/skills/{name}/SKILL.md
#   claude-skills → <target>/.claude/skills/{name}/SKILL.md (same path, fewer features)
#   codex         → <target>/.codex/skills/{name}/SKILL.md
#   gemini        → <target>/.gemini/skills/{name}.toml
#   antigravity   → <target>/.antigravity/commands/{name}.md

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ADAPTERS_DIR="$SCRIPT_DIR/adapters"

if [ $# -lt 1 ]; then
    echo "Usage: $0 <target-dir> [platform...]"
    echo ""
    echo "Platforms: claude-code, claude-skills, codex, gemini, antigravity"
    echo "Default: installs all detected platforms"
    exit 1
fi

TARGET="$(cd "$1" && pwd)"
shift

# Default: install all platforms
PLATFORMS=("${@:-claude-code codex gemini antigravity}")
if [ ${#PLATFORMS[@]} -eq 0 ] || [ "${PLATFORMS[0]}" = "claude-code codex gemini antigravity" ]; then
    PLATFORMS=(claude-code codex gemini antigravity)
fi

install_platform() {
    local platform="$1"
    local src_dir="$ADAPTERS_DIR/$platform"
    local dest_dir

    if [ ! -d "$src_dir" ]; then
        echo "  ⚠ Adapter not generated for $platform — run generate-adapters.py first"
        return 1
    fi

    case "$platform" in
        claude-code|claude-skills)
            dest_dir="$TARGET/.claude/skills"
            ;;
        codex)
            dest_dir="$TARGET/.codex/skills"
            ;;
        gemini)
            dest_dir="$TARGET/.gemini/skills"
            ;;
        antigravity)
            dest_dir="$TARGET/.antigravity/commands"
            ;;
        *)
            echo "  ⚠ Unknown platform: $platform"
            return 1
            ;;
    esac

    mkdir -p "$dest_dir"

    local count=0
    if [ "$platform" = "gemini" ]; then
        # Gemini: flat .toml files
        for f in "$src_dir"/*.toml; do
            [ -f "$f" ] || continue
            cp "$f" "$dest_dir/"
            count=$((count + 1))
        done
    elif [ "$platform" = "antigravity" ]; then
        # Antigravity: flat .md files
        for f in "$src_dir"/*.md; do
            [ -f "$f" ] || continue
            cp "$f" "$dest_dir/"
            count=$((count + 1))
        done
    else
        # Claude/Codex: {name}/SKILL.md directories
        for d in "$src_dir"/*/; do
            [ -d "$d" ] || continue
            local name
            name="$(basename "$d")"
            mkdir -p "$dest_dir/$name"
            cp "$d/SKILL.md" "$dest_dir/$name/SKILL.md"
            count=$((count + 1))
        done
    fi

    echo "  ✓ $platform → $dest_dir ($count skills)"
}

echo "Installing design skills to: $TARGET"
echo ""

for platform in "${PLATFORMS[@]}"; do
    install_platform "$platform"
done

echo ""
echo "Done! Skills installed."
