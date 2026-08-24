#!/usr/bin/env bash
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
assets="$here/assets"
mkdir -p "$assets"

download() {
    local url="$1"
    local name="$2"
    printf 'downloading %s\n' "$name"
    curl --fail --location --retry 3 --retry-delay 2 --output "$assets/$name" "$url"
}

download 'https://upload.wikimedia.org/wikipedia/commons/c/c6/Head_of_Hipparchus_%28cropped%29.jpg' 'Head of Hipparchus (cropped).jpg'
download 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Trigonometry_triangle.svg' 'Trigonometry triangle.svg'
download 'https://upload.wikimedia.org/wikipedia/commons/b/b5/Sin-cos-defn-I.png' 'Sin-cos-defn-I.png'
download 'https://upload.wikimedia.org/wikipedia/commons/3/35/Math_Trigonometry_Unit_Circle_Rotation_Sign_Indication.svg' 'Math Trigonometry Unit Circle Rotation Sign Indication.svg'
download 'https://upload.wikimedia.org/wikipedia/commons/d/d2/Sine_one_period.svg' 'Sine one period.svg'
download 'https://upload.wikimedia.org/wikipedia/commons/0/0a/Cosine_one_period.svg' 'Cosine one period.svg'
download 'https://upload.wikimedia.org/wikipedia/commons/7/74/Tangent-plot.svg' 'Tangent-plot.svg'
download 'https://upload.wikimedia.org/wikipedia/commons/7/73/Secant.svg' 'Secant.svg'
download 'https://upload.wikimedia.org/wikipedia/commons/0/0a/Cosecant.svg' 'Cosecant.svg'
download 'https://upload.wikimedia.org/wikipedia/commons/b/bf/Cotangent.svg' 'Cotangent.svg'
download 'https://upload.wikimedia.org/wikipedia/commons/2/2d/Frieberger_drum_marine_sextant.jpg' 'Frieberger drum marine sextant.jpg'
download 'https://upload.wikimedia.org/wikipedia/commons/2/2b/Fourier_series_and_transform.gif' 'Fourier series and transform.gif'
download 'https://upload.wikimedia.org/wikipedia/commons/2/24/Triangle_ABC_with_Sides_a_b_c_2.png' 'Triangle ABC with Sides a b c 2.png'

(
    cd "$assets"
    sha256sum \
      'Head of Hipparchus (cropped).jpg' \
      'Trigonometry triangle.svg' \
      'Sin-cos-defn-I.png' \
      'Math Trigonometry Unit Circle Rotation Sign Indication.svg' \
      'Sine one period.svg' \
      'Cosine one period.svg' \
      'Tangent-plot.svg' \
      'Secant.svg' \
      'Cosecant.svg' \
      'Cotangent.svg' \
      'Frieberger drum marine sextant.jpg' \
      'Fourier series and transform.gif' \
      'Triangle ABC with Sides a b c 2.png'
) > "$here/SHA256SUMS"
