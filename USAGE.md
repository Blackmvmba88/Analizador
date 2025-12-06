# Analizador Musical Completo

**Complete Musical Analysis System** - A comprehensive Python library for analyzing all aspects of musical compositions.

## Overview

This system provides in-depth analysis of musical compositions covering:

- **Metadata**: Title, artist, genre, release date, emotional intent
- **Form**: Intro, verses, pre-chorus, chorus, bridge, outro structure
- **Harmony**: Key, chords, progressions, cadences
- **Melody**: Motifs, contour, intervals, range
- **Rhythm**: Tempo, time signature, syncopation, groove
- **Texture**: Instruments, stereo width, dynamics, layers
- **Lyrics**: Theme, symbolism, prosody, rhyme scheme
- **Arrangement**: Production layers, contrast, effects
- **Mastering**: Loudness, EQ balance, dynamic range
- **Overall**: Emotional arc, market fit, strengths, improvements

## Installation

```bash
# Clone the repository
git clone https://github.com/Blackmvmba88/Analizador.git
cd Analizador

# No external dependencies required - uses Python standard library only
```

## Quick Start

```python
from analizador_musical import MusicalAnalyzer, create_example_analysis

# Create an analyzer instance
analyzer = MusicalAnalyzer()

# Analyze from a dictionary of musical data
musical_data = {
    "metadata": {
        "title": "My Song",
        "artist": "Artist Name",
        "genre": "Pop",
        "release_date": "2024-01-01",
        "duration": 180.0,
        "emotional_intent": ["happy", "energetic"]
    },
    "form": {
        "sections": [
            ("intro", 0.0, 8.0),
            ("verse", 8.0, 28.0),
            ("chorus", 28.0, 48.0),
            ("verse", 48.0, 68.0),
            ("chorus", 68.0, 88.0),
            ("bridge", 88.0, 108.0),
            ("chorus", 108.0, 128.0),
            ("outro", 128.0, 140.0)
        ],
        "total_duration": 140.0
    },
    "harmony": {
        "key": "G major",
        "mode": "major",
        "chords": ["G", "D", "Em", "C"],
        "chord_progression": "I-V-vi-IV",
        "harmonic_complexity": "simple"
    },
    # ... add other sections as needed
}

# Load the data
analyzer.analyze_from_dict(musical_data)

# Generate a human-readable report
print(analyzer.generate_report())

# Or get the analysis as a dictionary for further processing
analysis_dict = analyzer.get_complete_analysis()
```

## Example Output

Run the module directly to see an example analysis:

```bash
python analizador_musical.py
```

This will display a complete analysis report like:

```
================================================================================
COMPREHENSIVE MUSICAL ANALYSIS
================================================================================

METADATA
--------------------------------------------------------------------------------
Title: Example Song
Artist: Example Artist
Genre: Pop Rock
Release Date: 2024-01-15
Duration: 210.00 seconds
Emotional Intent: uplifting, energetic

FORM STRUCTURE
--------------------------------------------------------------------------------
Total Duration: 150.00 seconds
Sections:
  INTRO: 0.00s - 8.00s (8.00s)
  VERSE: 8.00s - 28.00s (20.00s)
  PRE-CHORUS: 28.00s - 36.00s (8.00s)
  CHORUS: 36.00s - 54.00s (18.00s)
  ...

[Full report continues with all analysis sections]
```

## Data Structure

### Metadata
```python
{
    "title": str,
    "artist": str,
    "genre": str,
    "release_date": str,  # ISO format: "YYYY-MM-DD"
    "duration": float,    # in seconds
    "emotional_intent": list[str]  # e.g., ["happy", "energetic"]
}
```

### Form Structure
```python
{
    "sections": [
        (section_name, start_time, end_time),  # e.g., ("verse", 8.0, 28.0)
    ],
    "total_duration": float
}
```

Section types: `intro`, `verse`, `pre-chorus`, `chorus`, `bridge`, `outro`, `interlude`, `solo`

### Harmony
```python
{
    "key": str,              # e.g., "C major", "A minor"
    "mode": str,             # "major" or "minor"
    "chords": list[str],     # e.g., ["C", "G", "Am", "F"]
    "chord_progression": str, # e.g., "I-V-vi-IV"
    "cadences": [(type, timestamp)],  # e.g., [("authentic", 53.5)]
    "modulations": [(new_key, timestamp)],
    "harmonic_complexity": str  # "simple", "moderate", "complex"
}
```

Cadence types: `authentic`, `half`, `plagal`, `deceptive`

### Melody
```python
{
    "motifs": list[str],          # e.g., ["ascending scale", "repeated hook"]
    "contour": str,               # "ascending", "descending", "arched", "wave", "static"
    "range_semitones": int,       # melodic range
    "intervals": list[str],       # e.g., ["major third", "perfect fifth"]
    "tessitura": str,             # "low", "medium", "high"
    "melodic_complexity": str     # "simple", "moderate", "complex"
}
```

### Rhythm
```python
{
    "tempo": int,                 # BPM
    "time_signature": str,        # e.g., "4/4", "3/4", "6/8"
    "syncopation_level": str,     # "low", "moderate", "high"
    "rhythmic_patterns": list[str],
    "groove": str,                # description
    "tempo_changes": [(new_tempo, timestamp)]
}
```

### Texture
```python
{
    "instruments": list[str],     # e.g., ["vocals", "guitar", "drums"]
    "stereo_width": str,          # "narrow", "medium", "wide"
    "dynamics_range": str,        # "compressed", "moderate", "wide"
    "texture_type": str,          # "monophonic", "homophonic", "polyphonic"
    "layers_count": int,
    "density": str                # "sparse", "moderate", "dense"
}
```

### Lyrics
```python
{
    "theme": str,
    "key_phrases": list[str],
    "symbolism": list[str],
    "prosody_quality": str,       # "poor", "good", "excellent"
    "rhyme_scheme": str,          # e.g., "AABB", "ABAB"
    "narrative_structure": str,   # "linear", "non-linear", "abstract"
    "language": str
}
```

### Arrangement
```python
{
    "layers": list[str],          # description of layers
    "contrast_sections": list[str],
    "effects_used": list[str],    # e.g., ["reverb", "delay", "chorus"]
    "production_style": str,      # "minimalist", "standard", "maximalist"
    "sonic_signature": str        # unique characteristics
}
```

### Mastering
```python
{
    "loudness_lufs": float,       # LUFS value
    "peak_db": float,             # peak level in dB
    "dynamic_range": float,       # in dB
    "eq_balance": str,            # "bass-heavy", "balanced", "bright"
    "stereo_imaging": str,        # "mono", "balanced", "wide"
    "compression_level": str      # "light", "moderate", "heavy"
}
```

### Overall Analysis
```python
{
    "emotional_arc": str,         # description of emotional journey
    "market_fit": str,            # target market analysis
    "strengths": list[str],
    "improvements": list[str],
    "commercial_potential": str,  # "low", "moderate", "high"
    "artistic_merit": str,        # "low", "moderate", "high"
    "overall_rating": float       # 0-10 scale
}
```

## Use Cases

### Music Production
Analyze your tracks to identify strengths and areas for improvement before releasing.

### Music Education
Teach students about musical form, harmony, and arrangement through detailed analysis.

### A&R and Music Business
Evaluate commercial potential and market fit of songs.

### Music Research
Collect and analyze data about musical trends and patterns.

### Personal Music Library
Document and catalog your music collection with detailed metadata.

## Advanced Usage

### Creating Custom Analyses

```python
from analizador_musical import (
    MusicalAnalyzer, Metadata, FormStructure, FormSection,
    EmotionalIntent, CadenceType, ContourType
)

# Create a new analyzer
analyzer = MusicalAnalyzer()

# Manually set metadata
analyzer.metadata.title = "My Song"
analyzer.metadata.artist = "My Band"
analyzer.metadata.emotional_intent = [
    EmotionalIntent.ENERGETIC,
    EmotionalIntent.UPLIFTING
]

# Add form sections
analyzer.form.add_section(FormSection.INTRO, 0.0, 8.0)
analyzer.form.add_section(FormSection.VERSE, 8.0, 28.0)
analyzer.form.add_section(FormSection.CHORUS, 28.0, 48.0)

# Set harmony information
analyzer.harmony.key = "D major"
analyzer.harmony.chord_progression = "I-V-vi-IV"
analyzer.harmony.cadences = [
    (CadenceType.AUTHENTIC, 47.5)
]

# Generate report
print(analyzer.generate_report())
```

### Exporting Analysis

```python
import json

# Get analysis as dictionary
analysis = analyzer.get_complete_analysis()

# Save to JSON file
with open('song_analysis.json', 'w') as f:
    json.dump(analysis, f, indent=2)

# Load from JSON file
with open('song_analysis.json', 'r') as f:
    data = json.load(f)
    
new_analyzer = MusicalAnalyzer()
new_analyzer.analyze_from_dict(data)
```

## API Reference

### MusicalAnalyzer Class

#### Methods

- `analyze_from_dict(data: Dict) -> MusicalAnalyzer`: Load analysis from dictionary
- `get_complete_analysis() -> Dict`: Export complete analysis as dictionary
- `generate_report() -> str`: Generate human-readable text report

#### Properties

- `metadata: Metadata`: Song metadata
- `form: FormStructure`: Form/structure analysis
- `harmony: HarmonyAnalysis`: Harmonic analysis
- `melody: MelodyAnalysis`: Melodic analysis
- `rhythm: RhythmAnalysis`: Rhythmic analysis
- `texture: TextureAnalysis`: Texture and instrumentation
- `lyrics: LyricsAnalysis`: Lyrical analysis
- `arrangement: ArrangementAnalysis`: Arrangement details
- `mastering: MasteringAnalysis`: Mastering information
- `overall: OverallAnalysis`: Overall evaluation

### Helper Functions

- `create_example_analysis() -> MusicalAnalyzer`: Creates a complete example analysis for reference

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.

## Author

Created for comprehensive musical analysis and education.
