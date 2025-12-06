"""
Test suite for Analizador Musical
"""

import json
from analizador_musical import (
    MusicalAnalyzer, 
    create_example_analysis,
    EmotionalIntent,
    FormSection,
    CadenceType,
    ContourType
)


def test_metadata():
    """Test metadata functionality"""
    analyzer = MusicalAnalyzer()
    analyzer.metadata.title = "Test Song"
    analyzer.metadata.artist = "Test Artist"
    analyzer.metadata.genre = "Test Genre"
    analyzer.metadata.emotional_intent = [EmotionalIntent.HAPPY]
    
    metadata_dict = analyzer.metadata.to_dict()
    assert metadata_dict["title"] == "Test Song"
    assert metadata_dict["artist"] == "Test Artist"
    assert metadata_dict["genre"] == "Test Genre"
    assert "happy" in metadata_dict["emotional_intent"]
    print("✓ Metadata test passed")


def test_form_structure():
    """Test form structure functionality"""
    analyzer = MusicalAnalyzer()
    analyzer.form.add_section(FormSection.INTRO, 0.0, 8.0)
    analyzer.form.add_section(FormSection.VERSE, 8.0, 28.0)
    analyzer.form.add_section(FormSection.CHORUS, 28.0, 48.0)
    
    assert len(analyzer.form.sections) == 3
    assert analyzer.form.get_section_count(FormSection.VERSE) == 1
    assert analyzer.form.get_section_count(FormSection.CHORUS) == 1
    
    form_dict = analyzer.form.to_dict()
    assert len(form_dict["sections"]) == 3
    print("✓ Form structure test passed")


def test_harmony_analysis():
    """Test harmony analysis functionality"""
    analyzer = MusicalAnalyzer()
    analyzer.harmony.key = "C major"
    analyzer.harmony.mode = "major"
    analyzer.harmony.chords = ["C", "G", "Am", "F"]
    analyzer.harmony.chord_progression = "I-V-vi-IV"
    analyzer.harmony.cadences = [(CadenceType.AUTHENTIC, 50.0)]
    
    harmony_dict = analyzer.harmony.to_dict()
    assert harmony_dict["key"] == "C major"
    assert harmony_dict["mode"] == "major"
    assert len(harmony_dict["chords"]) == 4
    assert len(harmony_dict["cadences"]) == 1
    print("✓ Harmony analysis test passed")


def test_melody_analysis():
    """Test melody analysis functionality"""
    analyzer = MusicalAnalyzer()
    analyzer.melody.contour = ContourType.ARCHED
    analyzer.melody.range_semitones = 12
    analyzer.melody.motifs = ["ascending scale", "repeated hook"]
    
    melody_dict = analyzer.melody.to_dict()
    assert melody_dict["contour"] == "arched"
    assert melody_dict["range_semitones"] == 12
    assert len(melody_dict["motifs"]) == 2
    print("✓ Melody analysis test passed")


def test_rhythm_analysis():
    """Test rhythm analysis functionality"""
    analyzer = MusicalAnalyzer()
    analyzer.rhythm.tempo = 120
    analyzer.rhythm.time_signature = "4/4"
    analyzer.rhythm.syncopation_level = "moderate"
    
    rhythm_dict = analyzer.rhythm.to_dict()
    assert rhythm_dict["tempo"] == 120
    assert rhythm_dict["time_signature"] == "4/4"
    assert rhythm_dict["syncopation_level"] == "moderate"
    print("✓ Rhythm analysis test passed")


def test_texture_analysis():
    """Test texture analysis functionality"""
    analyzer = MusicalAnalyzer()
    analyzer.texture.instruments = ["guitar", "bass", "drums"]
    analyzer.texture.layers_count = 5
    analyzer.texture.stereo_width = "wide"
    
    texture_dict = analyzer.texture.to_dict()
    assert len(texture_dict["instruments"]) == 3
    assert texture_dict["layers_count"] == 5
    assert texture_dict["stereo_width"] == "wide"
    print("✓ Texture analysis test passed")


def test_lyrics_analysis():
    """Test lyrics analysis functionality"""
    analyzer = MusicalAnalyzer()
    analyzer.lyrics.theme = "love"
    analyzer.lyrics.rhyme_scheme = "ABAB"
    analyzer.lyrics.key_phrases = ["forever", "together"]
    
    lyrics_dict = analyzer.lyrics.to_dict()
    assert lyrics_dict["theme"] == "love"
    assert lyrics_dict["rhyme_scheme"] == "ABAB"
    assert len(lyrics_dict["key_phrases"]) == 2
    print("✓ Lyrics analysis test passed")


def test_arrangement_analysis():
    """Test arrangement analysis functionality"""
    analyzer = MusicalAnalyzer()
    analyzer.arrangement.effects_used = ["reverb", "delay", "chorus"]
    analyzer.arrangement.production_style = "standard"
    
    arrangement_dict = analyzer.arrangement.to_dict()
    assert len(arrangement_dict["effects_used"]) == 3
    assert arrangement_dict["production_style"] == "standard"
    print("✓ Arrangement analysis test passed")


def test_mastering_analysis():
    """Test mastering analysis functionality"""
    analyzer = MusicalAnalyzer()
    analyzer.mastering.loudness_lufs = -10.0
    analyzer.mastering.peak_db = -1.0
    analyzer.mastering.dynamic_range = 8.0
    
    mastering_dict = analyzer.mastering.to_dict()
    assert mastering_dict["loudness_lufs"] == -10.0
    assert mastering_dict["peak_db"] == -1.0
    assert mastering_dict["dynamic_range"] == 8.0
    print("✓ Mastering analysis test passed")


def test_overall_analysis():
    """Test overall analysis functionality"""
    analyzer = MusicalAnalyzer()
    analyzer.overall.emotional_arc = "building to climax"
    analyzer.overall.market_fit = "pop radio"
    analyzer.overall.strengths = ["strong melody", "great production"]
    analyzer.overall.improvements = ["extend outro"]
    analyzer.overall.overall_rating = 8.5
    
    overall_dict = analyzer.overall.to_dict()
    assert overall_dict["emotional_arc"] == "building to climax"
    assert len(overall_dict["strengths"]) == 2
    assert len(overall_dict["improvements"]) == 1
    assert overall_dict["overall_rating"] == 8.5
    print("✓ Overall analysis test passed")


def test_complete_analysis():
    """Test complete analysis workflow"""
    analyzer = create_example_analysis()
    
    # Test report generation
    report = analyzer.generate_report()
    assert "COMPREHENSIVE MUSICAL ANALYSIS" in report
    assert "Example Song" in report
    assert "Example Artist" in report
    
    # Test dictionary export
    analysis_dict = analyzer.get_complete_analysis()
    assert "metadata" in analysis_dict
    assert "form" in analysis_dict
    assert "harmony" in analysis_dict
    assert "melody" in analysis_dict
    assert "rhythm" in analysis_dict
    assert "texture" in analysis_dict
    assert "lyrics" in analysis_dict
    assert "arrangement" in analysis_dict
    assert "mastering" in analysis_dict
    assert "overall" in analysis_dict
    
    print("✓ Complete analysis test passed")


def test_analyze_from_dict():
    """Test loading analysis from dictionary"""
    test_data = {
        "metadata": {
            "title": "Test Song",
            "artist": "Test Artist",
            "genre": "Rock",
            "release_date": "2024-01-01",
            "duration": 180.0,
            "emotional_intent": ["energetic"]
        },
        "harmony": {
            "key": "D major",
            "mode": "major",
            "chords": ["D", "A", "Bm", "G"],
            "chord_progression": "I-V-vi-IV",
            "harmonic_complexity": "simple"
        },
        "rhythm": {
            "tempo": 140,
            "time_signature": "4/4",
            "syncopation_level": "low"
        }
    }
    
    analyzer = MusicalAnalyzer()
    analyzer.analyze_from_dict(test_data)
    
    assert analyzer.metadata.title == "Test Song"
    assert analyzer.metadata.artist == "Test Artist"
    assert analyzer.harmony.key == "D major"
    assert analyzer.rhythm.tempo == 140
    
    print("✓ Analyze from dict test passed")


def test_json_serialization():
    """Test JSON serialization and deserialization"""
    # Create an analyzer with example data
    analyzer1 = create_example_analysis()
    
    # Export to dictionary
    analysis_dict = analyzer1.get_complete_analysis()
    
    # Serialize to JSON string
    json_str = json.dumps(analysis_dict, indent=2)
    assert len(json_str) > 0
    
    # Deserialize from JSON
    loaded_dict = json.loads(json_str)
    
    # Create new analyzer from loaded data
    analyzer2 = MusicalAnalyzer()
    analyzer2.analyze_from_dict(loaded_dict)
    
    # Verify data matches
    assert analyzer2.metadata.title == analyzer1.metadata.title
    assert analyzer2.metadata.artist == analyzer1.metadata.artist
    assert analyzer2.harmony.key == analyzer1.harmony.key
    assert analyzer2.rhythm.tempo == analyzer1.rhythm.tempo
    
    print("✓ JSON serialization test passed")


def run_all_tests():
    """Run all tests"""
    print("Running Analizador Musical Tests...\n")
    
    test_metadata()
    test_form_structure()
    test_harmony_analysis()
    test_melody_analysis()
    test_rhythm_analysis()
    test_texture_analysis()
    test_lyrics_analysis()
    test_arrangement_analysis()
    test_mastering_analysis()
    test_overall_analysis()
    test_complete_analysis()
    test_analyze_from_dict()
    test_json_serialization()
    
    print("\n" + "=" * 50)
    print("All tests passed! ✓")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
