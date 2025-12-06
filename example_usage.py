#!/usr/bin/env python
"""
Example: Analyzing a custom song
This example demonstrates how to create a musical analysis for your own song.
"""

import json
from analizador_musical import MusicalAnalyzer, EmotionalIntent, FormSection, ContourType

def analyze_custom_song():
    """Example of analyzing a custom song"""
    
    print("Creating analysis for 'Sunset Boulevard'...\n")
    
    # Create a new analyzer
    analyzer = MusicalAnalyzer()
    
    # Set metadata
    analyzer.metadata.title = "Sunset Boulevard"
    analyzer.metadata.artist = "The Dreamers"
    analyzer.metadata.genre = "Indie Rock"
    analyzer.metadata.release_date = "2024-06-15"
    analyzer.metadata.duration = 195.0
    analyzer.metadata.emotional_intent = [
        EmotionalIntent.MELANCHOLIC,
        EmotionalIntent.NOSTALGIC
    ]
    
    # Define form structure
    analyzer.form.add_section(FormSection.INTRO, 0.0, 12.0)
    analyzer.form.add_section(FormSection.VERSE, 12.0, 35.0)
    analyzer.form.add_section(FormSection.VERSE, 35.0, 58.0)
    analyzer.form.add_section(FormSection.CHORUS, 58.0, 78.0)
    analyzer.form.add_section(FormSection.VERSE, 78.0, 101.0)
    analyzer.form.add_section(FormSection.CHORUS, 101.0, 121.0)
    analyzer.form.add_section(FormSection.BRIDGE, 121.0, 145.0)
    analyzer.form.add_section(FormSection.CHORUS, 145.0, 165.0)
    analyzer.form.add_section(FormSection.OUTRO, 165.0, 195.0)
    analyzer.form.total_duration = 195.0
    
    # Set harmony information
    analyzer.harmony.key = "E minor"
    analyzer.harmony.mode = "minor"
    analyzer.harmony.chords = ["Em", "C", "G", "D", "Am", "B7"]
    analyzer.harmony.chord_progression = "i-VI-III-VII"
    analyzer.harmony.harmonic_complexity = "moderate"
    
    # Set melody information
    analyzer.melody.motifs = ["descending minor scale", "suspended 4th resolution"]
    analyzer.melody.contour = ContourType.DESCENDING
    analyzer.melody.range_semitones = 16
    analyzer.melody.intervals = ["minor third", "perfect fourth", "major second"]
    analyzer.melody.tessitura = "medium"
    analyzer.melody.melodic_complexity = "moderate"
    
    # Set rhythm information
    analyzer.rhythm.tempo = 85
    analyzer.rhythm.time_signature = "4/4"
    analyzer.rhythm.syncopation_level = "low"
    analyzer.rhythm.rhythmic_patterns = ["steady quarter notes", "half-time feel in verses"]
    analyzer.rhythm.groove = "slow, walking tempo with emphasis on backbeat"
    
    # Set texture information
    analyzer.texture.instruments = [
        "lead vocals", "backing vocals", "acoustic guitar", 
        "electric guitar", "bass", "drums", "piano", "strings"
    ]
    analyzer.texture.stereo_width = "wide"
    analyzer.texture.dynamics_range = "wide"
    analyzer.texture.texture_type = "homophonic"
    analyzer.texture.layers_count = 12
    analyzer.texture.density = "moderate to dense"
    
    # Set lyrics information
    analyzer.lyrics.theme = "nostalgia for past relationships and simpler times"
    analyzer.lyrics.key_phrases = [
        "sunset boulevard", "memories fade like photographs", 
        "we were young", "golden hour"
    ]
    analyzer.lyrics.symbolism = [
        "sunset as passage of time",
        "boulevard as life's journey",
        "photographs as fading memories"
    ]
    analyzer.lyrics.prosody_quality = "excellent"
    analyzer.lyrics.rhyme_scheme = "ABCB"
    analyzer.lyrics.narrative_structure = "linear with flashbacks"
    analyzer.lyrics.language = "English"
    
    # Set arrangement information
    analyzer.arrangement.layers = [
        "intro: sparse acoustic guitar and vocals",
        "verse: add bass and light drums",
        "chorus: full band with strings",
        "bridge: piano feature with minimal backing"
    ]
    analyzer.arrangement.contrast_sections = [
        "verse to chorus dynamics",
        "bridge breakdown"
    ]
    analyzer.arrangement.effects_used = [
        "reverb", "delay", "plate reverb on vocals", 
        "tape saturation", "spring reverb on guitar"
    ]
    analyzer.arrangement.production_style = "vintage-inspired indie"
    analyzer.arrangement.sonic_signature = "warm, analog-style production with lush strings"
    
    # Set mastering information
    analyzer.mastering.loudness_lufs = -12.0
    analyzer.mastering.peak_db = -0.8
    analyzer.mastering.dynamic_range = 9.5
    analyzer.mastering.eq_balance = "warm with emphasized low-mids"
    analyzer.mastering.stereo_imaging = "wide"
    analyzer.mastering.compression_level = "light"
    
    # Set overall analysis
    analyzer.overall.emotional_arc = (
        "Opens with wistful contemplation, builds through verses with growing "
        "intensity of emotion, chorus provides cathartic release, bridge offers "
        "moment of reflection, final chorus brings acceptance and closure"
    )
    analyzer.overall.market_fit = (
        "Perfect for indie rock/alternative radio and streaming playlists. "
        "Appeals to fans of Bon Iver, Fleet Foxes, and The National. "
        "Suitable for sync licensing in film/TV emotional scenes."
    )
    analyzer.overall.strengths = [
        "Evocative and poetic lyrics",
        "Strong emotional resonance",
        "Professional production with vintage character",
        "Well-crafted dynamic arc",
        "Memorable hook in chorus",
        "Effective use of strings for emotional impact"
    ]
    analyzer.overall.improvements = [
        "Second verse could use more variation to maintain interest",
        "Consider shortening outro by 5-10 seconds for radio edit",
        "Bridge could benefit from more instrumental texture",
        "Backing vocals in final chorus could be more prominent"
    ]
    analyzer.overall.commercial_potential = "moderate to high"
    analyzer.overall.artistic_merit = "high"
    analyzer.overall.overall_rating = 8.7
    
    # Generate and print report
    print(analyzer.generate_report())
    
    # Save to JSON file
    print("\nSaving analysis to sunset_boulevard_analysis.json...")
    with open('sunset_boulevard_analysis.json', 'w') as f:
        json.dump(analyzer.get_complete_analysis(), f, indent=2)
    print("✓ Analysis saved successfully!")
    
    return analyzer


def load_and_display_analysis():
    """Example of loading an analysis from JSON"""
    print("\n" + "=" * 80)
    print("Loading analysis from JSON file...")
    print("=" * 80 + "\n")
    
    try:
        with open('sunset_boulevard_analysis.json', 'r') as f:
            data = json.load(f)
        
        analyzer = MusicalAnalyzer()
        analyzer.analyze_from_dict(data)
        
        print(f"Loaded analysis for: {analyzer.metadata.title}")
        print(f"Artist: {analyzer.metadata.artist}")
        print(f"Genre: {analyzer.metadata.genre}")
        print(f"Overall Rating: {analyzer.overall.overall_rating}/10")
        print("\nStrengths:")
        for strength in analyzer.overall.strengths:
            print(f"  + {strength}")
        
    except FileNotFoundError:
        print("Analysis file not found. Run analyze_custom_song() first.")


if __name__ == "__main__":
    # Create and analyze a custom song
    analyzer = analyze_custom_song()
    
    # Demonstrate loading from file
    load_and_display_analysis()
