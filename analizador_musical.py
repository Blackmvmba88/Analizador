"""
Analizador Musical Completo
Complete Musical Analysis System

This module provides comprehensive musical analysis capabilities including:
- Metadata analysis (title, artist, genre, release, emotional intent)
- Form analysis (intro, verses, pre-chorus, chorus, bridge, outro)
- Harmony analysis (key, chords, cadences)
- Melody analysis (motifs, contour, intervals)
- Rhythm analysis (tempo, syncopation)
- Texture analysis (instruments, stereo, dynamics)
- Lyrics analysis (theme, symbolism, prosody)
- Arrangement analysis (layers, contrast, FX)
- Mastering analysis (loudness, EQ)
- Overall analysis (emotional arc, market fit, strengths and improvements)
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum


class EmotionalIntent(Enum):
    """Emotional intent categories"""
    HAPPY = "happy"
    SAD = "sad"
    ENERGETIC = "energetic"
    CALM = "calm"
    AGGRESSIVE = "aggressive"
    MELANCHOLIC = "melancholic"
    ROMANTIC = "romantic"
    NOSTALGIC = "nostalgic"
    UPLIFTING = "uplifting"
    DARK = "dark"


class FormSection(Enum):
    """Musical form sections"""
    INTRO = "intro"
    VERSE = "verse"
    PRE_CHORUS = "pre-chorus"
    CHORUS = "chorus"
    BRIDGE = "bridge"
    OUTRO = "outro"
    INTERLUDE = "interlude"
    SOLO = "solo"


class CadenceType(Enum):
    """Types of harmonic cadences"""
    AUTHENTIC = "authentic"
    HALF = "half"
    PLAGAL = "plagal"
    DECEPTIVE = "deceptive"


class ContourType(Enum):
    """Melodic contour types"""
    ASCENDING = "ascending"
    DESCENDING = "descending"
    ARCHED = "arched"
    WAVE = "wave"
    STATIC = "static"


@dataclass
class Metadata:
    """Musical metadata information"""
    title: str = ""
    artist: str = ""
    genre: str = ""
    release_date: str = ""
    emotional_intent: List[EmotionalIntent] = field(default_factory=list)
    duration: float = 0.0  # in seconds
    
    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "artist": self.artist,
            "genre": self.genre,
            "release_date": self.release_date,
            "emotional_intent": [ei.value for ei in self.emotional_intent],
            "duration": self.duration
        }


@dataclass
class FormStructure:
    """Musical form structure"""
    sections: List[Tuple[FormSection, float, float]] = field(default_factory=list)  # (section, start_time, end_time)
    total_duration: float = 0.0
    
    def add_section(self, section: FormSection, start_time: float, end_time: float):
        """Add a section to the form"""
        self.sections.append((section, start_time, end_time))
        
    def get_section_count(self, section_type: FormSection) -> int:
        """Count occurrences of a specific section"""
        return sum(1 for s, _, _ in self.sections if s == section_type)
    
    def to_dict(self) -> Dict:
        return {
            "sections": [(s.value, start, end) for s, start, end in self.sections],
            "total_duration": self.total_duration,
            "structure_summary": self._get_structure_summary()
        }
    
    def _get_structure_summary(self) -> str:
        """Get a summary of the form structure"""
        return " - ".join([s.value for s, _, _ in self.sections])


@dataclass
class HarmonyAnalysis:
    """Harmonic analysis"""
    key: str = ""  # e.g., "C major", "A minor"
    mode: str = ""  # "major" or "minor"
    chords: List[str] = field(default_factory=list)  # List of chords used
    chord_progression: str = ""  # e.g., "I-V-vi-IV"
    cadences: List[Tuple[CadenceType, float]] = field(default_factory=list)  # (type, timestamp)
    modulations: List[Tuple[str, float]] = field(default_factory=list)  # (new_key, timestamp)
    harmonic_complexity: str = ""  # "simple", "moderate", "complex"
    
    def to_dict(self) -> Dict:
        return {
            "key": self.key,
            "mode": self.mode,
            "chords": self.chords,
            "chord_progression": self.chord_progression,
            "cadences": [(c.value, t) for c, t in self.cadences],
            "modulations": self.modulations,
            "harmonic_complexity": self.harmonic_complexity
        }


@dataclass
class MelodyAnalysis:
    """Melodic analysis"""
    motifs: List[str] = field(default_factory=list)  # Recurring melodic patterns
    contour: ContourType = ContourType.WAVE
    range_semitones: int = 0  # Melodic range in semitones
    intervals: List[str] = field(default_factory=list)  # Common intervals used
    tessitura: str = ""  # "low", "medium", "high"
    melodic_complexity: str = ""  # "simple", "moderate", "complex"
    
    def to_dict(self) -> Dict:
        return {
            "motifs": self.motifs,
            "contour": self.contour.value,
            "range_semitones": self.range_semitones,
            "intervals": self.intervals,
            "tessitura": self.tessitura,
            "melodic_complexity": self.melodic_complexity
        }


@dataclass
class RhythmAnalysis:
    """Rhythmic analysis"""
    tempo: int = 120  # BPM
    time_signature: str = "4/4"
    syncopation_level: str = ""  # "low", "moderate", "high"
    rhythmic_patterns: List[str] = field(default_factory=list)
    groove: str = ""  # Description of the groove
    tempo_changes: List[Tuple[int, float]] = field(default_factory=list)  # (new_tempo, timestamp)
    
    def to_dict(self) -> Dict:
        return {
            "tempo": self.tempo,
            "time_signature": self.time_signature,
            "syncopation_level": self.syncopation_level,
            "rhythmic_patterns": self.rhythmic_patterns,
            "groove": self.groove,
            "tempo_changes": self.tempo_changes
        }


@dataclass
class TextureAnalysis:
    """Texture and instrumentation analysis"""
    instruments: List[str] = field(default_factory=list)
    stereo_width: str = ""  # "narrow", "medium", "wide"
    dynamics_range: str = ""  # "compressed", "moderate", "wide"
    texture_type: str = ""  # "monophonic", "homophonic", "polyphonic"
    layers_count: int = 0
    density: str = ""  # "sparse", "moderate", "dense"
    
    def to_dict(self) -> Dict:
        return {
            "instruments": self.instruments,
            "stereo_width": self.stereo_width,
            "dynamics_range": self.dynamics_range,
            "texture_type": self.texture_type,
            "layers_count": self.layers_count,
            "density": self.density
        }


@dataclass
class LyricsAnalysis:
    """Lyrics analysis"""
    theme: str = ""
    key_phrases: List[str] = field(default_factory=list)
    symbolism: List[str] = field(default_factory=list)
    prosody_quality: str = ""  # "poor", "good", "excellent"
    rhyme_scheme: str = ""  # e.g., "AABB", "ABAB"
    narrative_structure: str = ""  # "linear", "non-linear", "abstract"
    language: str = ""
    
    def to_dict(self) -> Dict:
        return {
            "theme": self.theme,
            "key_phrases": self.key_phrases,
            "symbolism": self.symbolism,
            "prosody_quality": self.prosody_quality,
            "rhyme_scheme": self.rhyme_scheme,
            "narrative_structure": self.narrative_structure,
            "language": self.language
        }


@dataclass
class ArrangementAnalysis:
    """Arrangement analysis"""
    layers: List[str] = field(default_factory=list)  # Different arrangement layers
    contrast_sections: List[str] = field(default_factory=list)  # Sections with notable contrast
    effects_used: List[str] = field(default_factory=list)  # Reverb, delay, chorus, etc.
    production_style: str = ""  # "minimalist", "standard", "maximalist"
    sonic_signature: str = ""  # Unique production characteristics
    
    def to_dict(self) -> Dict:
        return {
            "layers": self.layers,
            "contrast_sections": self.contrast_sections,
            "effects_used": self.effects_used,
            "production_style": self.production_style,
            "sonic_signature": self.sonic_signature
        }


@dataclass
class MasteringAnalysis:
    """Mastering and final production analysis"""
    loudness_lufs: float = -14.0  # LUFS (Loudness Units Full Scale)
    peak_db: float = -1.0  # Peak level in dB
    dynamic_range: float = 8.0  # Dynamic range in dB
    eq_balance: str = ""  # "bass-heavy", "balanced", "bright"
    stereo_imaging: str = ""  # "mono", "balanced", "wide"
    compression_level: str = ""  # "light", "moderate", "heavy"
    
    def to_dict(self) -> Dict:
        return {
            "loudness_lufs": self.loudness_lufs,
            "peak_db": self.peak_db,
            "dynamic_range": self.dynamic_range,
            "eq_balance": self.eq_balance,
            "stereo_imaging": self.stereo_imaging,
            "compression_level": self.compression_level
        }


@dataclass
class OverallAnalysis:
    """Overall musical analysis and evaluation"""
    emotional_arc: str = ""  # Description of emotional journey
    market_fit: str = ""  # Target market and genre fit
    strengths: List[str] = field(default_factory=list)
    improvements: List[str] = field(default_factory=list)
    commercial_potential: str = ""  # "low", "moderate", "high"
    artistic_merit: str = ""  # "low", "moderate", "high"
    overall_rating: float = 0.0  # 0-10 scale
    
    def to_dict(self) -> Dict:
        return {
            "emotional_arc": self.emotional_arc,
            "market_fit": self.market_fit,
            "strengths": self.strengths,
            "improvements": self.improvements,
            "commercial_potential": self.commercial_potential,
            "artistic_merit": self.artistic_merit,
            "overall_rating": self.overall_rating
        }


class MusicalAnalyzer:
    """Complete musical analyzer"""
    
    def __init__(self):
        self.metadata = Metadata()
        self.form = FormStructure()
        self.harmony = HarmonyAnalysis()
        self.melody = MelodyAnalysis()
        self.rhythm = RhythmAnalysis()
        self.texture = TextureAnalysis()
        self.lyrics = LyricsAnalysis()
        self.arrangement = ArrangementAnalysis()
        self.mastering = MasteringAnalysis()
        self.overall = OverallAnalysis()
    
    def analyze_from_dict(self, data: Dict) -> 'MusicalAnalyzer':
        """
        Populate analyzer from a dictionary of musical data.
        This is the main entry point for analysis.
        """
        # Metadata
        if "metadata" in data:
            md = data["metadata"]
            self.metadata.title = md.get("title", "")
            self.metadata.artist = md.get("artist", "")
            self.metadata.genre = md.get("genre", "")
            self.metadata.release_date = md.get("release_date", "")
            self.metadata.duration = md.get("duration", 0.0)
            # Parse emotional intent
            for ei in md.get("emotional_intent", []):
                try:
                    self.metadata.emotional_intent.append(EmotionalIntent(ei))
                except ValueError:
                    pass
        
        # Form
        if "form" in data:
            form_data = data["form"]
            for section_data in form_data.get("sections", []):
                try:
                    section = FormSection(section_data[0])
                    start = section_data[1]
                    end = section_data[2]
                    self.form.add_section(section, start, end)
                except (ValueError, IndexError):
                    pass
            self.form.total_duration = form_data.get("total_duration", 0.0)
        
        # Harmony
        if "harmony" in data:
            hm = data["harmony"]
            self.harmony.key = hm.get("key", "")
            self.harmony.mode = hm.get("mode", "")
            self.harmony.chords = hm.get("chords", [])
            self.harmony.chord_progression = hm.get("chord_progression", "")
            self.harmony.harmonic_complexity = hm.get("harmonic_complexity", "")
            # Parse cadences
            for cad in hm.get("cadences", []):
                try:
                    self.harmony.cadences.append((CadenceType(cad[0]), cad[1]))
                except (ValueError, IndexError):
                    pass
            self.harmony.modulations = hm.get("modulations", [])
        
        # Melody
        if "melody" in data:
            ml = data["melody"]
            self.melody.motifs = ml.get("motifs", [])
            contour_str = ml.get("contour", "wave")
            try:
                self.melody.contour = ContourType(contour_str)
            except ValueError:
                self.melody.contour = ContourType.WAVE
            self.melody.range_semitones = ml.get("range_semitones", 0)
            self.melody.intervals = ml.get("intervals", [])
            self.melody.tessitura = ml.get("tessitura", "")
            self.melody.melodic_complexity = ml.get("melodic_complexity", "")
        
        # Rhythm
        if "rhythm" in data:
            rt = data["rhythm"]
            self.rhythm.tempo = rt.get("tempo", 120)
            self.rhythm.time_signature = rt.get("time_signature", "4/4")
            self.rhythm.syncopation_level = rt.get("syncopation_level", "")
            self.rhythm.rhythmic_patterns = rt.get("rhythmic_patterns", [])
            self.rhythm.groove = rt.get("groove", "")
            self.rhythm.tempo_changes = rt.get("tempo_changes", [])
        
        # Texture
        if "texture" in data:
            tx = data["texture"]
            self.texture.instruments = tx.get("instruments", [])
            self.texture.stereo_width = tx.get("stereo_width", "")
            self.texture.dynamics_range = tx.get("dynamics_range", "")
            self.texture.texture_type = tx.get("texture_type", "")
            self.texture.layers_count = tx.get("layers_count", 0)
            self.texture.density = tx.get("density", "")
        
        # Lyrics
        if "lyrics" in data:
            ly = data["lyrics"]
            self.lyrics.theme = ly.get("theme", "")
            self.lyrics.key_phrases = ly.get("key_phrases", [])
            self.lyrics.symbolism = ly.get("symbolism", [])
            self.lyrics.prosody_quality = ly.get("prosody_quality", "")
            self.lyrics.rhyme_scheme = ly.get("rhyme_scheme", "")
            self.lyrics.narrative_structure = ly.get("narrative_structure", "")
            self.lyrics.language = ly.get("language", "")
        
        # Arrangement
        if "arrangement" in data:
            ar = data["arrangement"]
            self.arrangement.layers = ar.get("layers", [])
            self.arrangement.contrast_sections = ar.get("contrast_sections", [])
            self.arrangement.effects_used = ar.get("effects_used", [])
            self.arrangement.production_style = ar.get("production_style", "")
            self.arrangement.sonic_signature = ar.get("sonic_signature", "")
        
        # Mastering
        if "mastering" in data:
            ms = data["mastering"]
            self.mastering.loudness_lufs = ms.get("loudness_lufs", -14.0)
            self.mastering.peak_db = ms.get("peak_db", -1.0)
            self.mastering.dynamic_range = ms.get("dynamic_range", 8.0)
            self.mastering.eq_balance = ms.get("eq_balance", "")
            self.mastering.stereo_imaging = ms.get("stereo_imaging", "")
            self.mastering.compression_level = ms.get("compression_level", "")
        
        # Overall
        if "overall" in data:
            ov = data["overall"]
            self.overall.emotional_arc = ov.get("emotional_arc", "")
            self.overall.market_fit = ov.get("market_fit", "")
            self.overall.strengths = ov.get("strengths", [])
            self.overall.improvements = ov.get("improvements", [])
            self.overall.commercial_potential = ov.get("commercial_potential", "")
            self.overall.artistic_merit = ov.get("artistic_merit", "")
            self.overall.overall_rating = ov.get("overall_rating", 0.0)
        
        return self
    
    def get_complete_analysis(self) -> Dict:
        """Get the complete analysis as a dictionary"""
        return {
            "metadata": self.metadata.to_dict(),
            "form": self.form.to_dict(),
            "harmony": self.harmony.to_dict(),
            "melody": self.melody.to_dict(),
            "rhythm": self.rhythm.to_dict(),
            "texture": self.texture.to_dict(),
            "lyrics": self.lyrics.to_dict(),
            "arrangement": self.arrangement.to_dict(),
            "mastering": self.mastering.to_dict(),
            "overall": self.overall.to_dict()
        }
    
    def generate_report(self) -> str:
        """Generate a human-readable analysis report"""
        report = []
        report.append("=" * 80)
        report.append("COMPREHENSIVE MUSICAL ANALYSIS")
        report.append("=" * 80)
        report.append("")
        
        # Metadata
        report.append("METADATA")
        report.append("-" * 80)
        report.append(f"Title: {self.metadata.title}")
        report.append(f"Artist: {self.metadata.artist}")
        report.append(f"Genre: {self.metadata.genre}")
        report.append(f"Release Date: {self.metadata.release_date}")
        report.append(f"Duration: {self.metadata.duration:.2f} seconds")
        report.append(f"Emotional Intent: {', '.join([ei.value for ei in self.metadata.emotional_intent])}")
        report.append("")
        
        # Form
        report.append("FORM STRUCTURE")
        report.append("-" * 80)
        report.append(f"Total Duration: {self.form.total_duration:.2f} seconds")
        report.append("Sections:")
        for section, start, end in self.form.sections:
            report.append(f"  {section.value.upper()}: {start:.2f}s - {end:.2f}s ({end-start:.2f}s)")
        report.append(f"Structure: {self.form._get_structure_summary()}")
        report.append("")
        
        # Harmony
        report.append("HARMONY")
        report.append("-" * 80)
        report.append(f"Key: {self.harmony.key}")
        report.append(f"Mode: {self.harmony.mode}")
        report.append(f"Chord Progression: {self.harmony.chord_progression}")
        report.append(f"Chords Used: {', '.join(self.harmony.chords)}")
        report.append(f"Harmonic Complexity: {self.harmony.harmonic_complexity}")
        if self.harmony.cadences:
            report.append("Cadences:")
            for cad_type, time in self.harmony.cadences:
                report.append(f"  {cad_type.value} at {time:.2f}s")
        report.append("")
        
        # Melody
        report.append("MELODY")
        report.append("-" * 80)
        report.append(f"Contour: {self.melody.contour.value}")
        report.append(f"Range: {self.melody.range_semitones} semitones")
        report.append(f"Tessitura: {self.melody.tessitura}")
        report.append(f"Common Intervals: {', '.join(self.melody.intervals)}")
        report.append(f"Melodic Complexity: {self.melody.melodic_complexity}")
        if self.melody.motifs:
            report.append(f"Motifs: {', '.join(self.melody.motifs)}")
        report.append("")
        
        # Rhythm
        report.append("RHYTHM")
        report.append("-" * 80)
        report.append(f"Tempo: {self.rhythm.tempo} BPM")
        report.append(f"Time Signature: {self.rhythm.time_signature}")
        report.append(f"Syncopation Level: {self.rhythm.syncopation_level}")
        report.append(f"Groove: {self.rhythm.groove}")
        if self.rhythm.rhythmic_patterns:
            report.append(f"Rhythmic Patterns: {', '.join(self.rhythm.rhythmic_patterns)}")
        report.append("")
        
        # Texture
        report.append("TEXTURE")
        report.append("-" * 80)
        report.append(f"Instruments: {', '.join(self.texture.instruments)}")
        report.append(f"Texture Type: {self.texture.texture_type}")
        report.append(f"Layers: {self.texture.layers_count}")
        report.append(f"Density: {self.texture.density}")
        report.append(f"Stereo Width: {self.texture.stereo_width}")
        report.append(f"Dynamics Range: {self.texture.dynamics_range}")
        report.append("")
        
        # Lyrics
        report.append("LYRICS")
        report.append("-" * 80)
        report.append(f"Theme: {self.lyrics.theme}")
        report.append(f"Language: {self.lyrics.language}")
        report.append(f"Rhyme Scheme: {self.lyrics.rhyme_scheme}")
        report.append(f"Narrative Structure: {self.lyrics.narrative_structure}")
        report.append(f"Prosody Quality: {self.lyrics.prosody_quality}")
        if self.lyrics.key_phrases:
            report.append(f"Key Phrases: {', '.join(self.lyrics.key_phrases)}")
        if self.lyrics.symbolism:
            report.append(f"Symbolism: {', '.join(self.lyrics.symbolism)}")
        report.append("")
        
        # Arrangement
        report.append("ARRANGEMENT")
        report.append("-" * 80)
        report.append(f"Production Style: {self.arrangement.production_style}")
        report.append(f"Sonic Signature: {self.arrangement.sonic_signature}")
        if self.arrangement.layers:
            report.append(f"Layers: {', '.join(self.arrangement.layers)}")
        if self.arrangement.effects_used:
            report.append(f"Effects Used: {', '.join(self.arrangement.effects_used)}")
        if self.arrangement.contrast_sections:
            report.append(f"Contrast Sections: {', '.join(self.arrangement.contrast_sections)}")
        report.append("")
        
        # Mastering
        report.append("MASTERING")
        report.append("-" * 80)
        report.append(f"Loudness: {self.mastering.loudness_lufs:.2f} LUFS")
        report.append(f"Peak Level: {self.mastering.peak_db:.2f} dB")
        report.append(f"Dynamic Range: {self.mastering.dynamic_range:.2f} dB")
        report.append(f"EQ Balance: {self.mastering.eq_balance}")
        report.append(f"Stereo Imaging: {self.mastering.stereo_imaging}")
        report.append(f"Compression Level: {self.mastering.compression_level}")
        report.append("")
        
        # Overall
        report.append("OVERALL ANALYSIS")
        report.append("-" * 80)
        report.append(f"Emotional Arc: {self.overall.emotional_arc}")
        report.append(f"Market Fit: {self.overall.market_fit}")
        report.append(f"Commercial Potential: {self.overall.commercial_potential}")
        report.append(f"Artistic Merit: {self.overall.artistic_merit}")
        report.append(f"Overall Rating: {self.overall.overall_rating:.1f}/10")
        report.append("")
        if self.overall.strengths:
            report.append("STRENGTHS:")
            for strength in self.overall.strengths:
                report.append(f"  + {strength}")
            report.append("")
        if self.overall.improvements:
            report.append("SUGGESTED IMPROVEMENTS:")
            for improvement in self.overall.improvements:
                report.append(f"  - {improvement}")
            report.append("")
        
        report.append("=" * 80)
        
        return "\n".join(report)


def create_example_analysis() -> MusicalAnalyzer:
    """Create an example musical analysis"""
    example_data = {
        "metadata": {
            "title": "Example Song",
            "artist": "Example Artist",
            "genre": "Pop Rock",
            "release_date": "2024-01-15",
            "duration": 210.0,
            "emotional_intent": ["uplifting", "energetic"]
        },
        "form": {
            "sections": [
                ("intro", 0.0, 8.0),
                ("verse", 8.0, 28.0),
                ("pre-chorus", 28.0, 36.0),
                ("chorus", 36.0, 54.0),
                ("verse", 54.0, 74.0),
                ("pre-chorus", 74.0, 82.0),
                ("chorus", 82.0, 100.0),
                ("bridge", 100.0, 120.0),
                ("chorus", 120.0, 138.0),
                ("outro", 138.0, 150.0)
            ],
            "total_duration": 150.0
        },
        "harmony": {
            "key": "C major",
            "mode": "major",
            "chords": ["C", "G", "Am", "F", "Dm", "Em"],
            "chord_progression": "I-V-vi-IV",
            "cadences": [("authentic", 53.5), ("half", 81.5), ("authentic", 137.5)],
            "modulations": [],
            "harmonic_complexity": "moderate"
        },
        "melody": {
            "motifs": ["ascending scale", "repeated hook"],
            "contour": "arched",
            "range_semitones": 14,
            "intervals": ["major third", "perfect fifth", "major second"],
            "tessitura": "medium",
            "melodic_complexity": "moderate"
        },
        "rhythm": {
            "tempo": 128,
            "time_signature": "4/4",
            "syncopation_level": "moderate",
            "rhythmic_patterns": ["straight eighth notes", "syncopated pre-chorus"],
            "groove": "driving rock beat",
            "tempo_changes": []
        },
        "texture": {
            "instruments": ["vocals", "electric guitar", "bass", "drums", "synthesizer", "piano"],
            "stereo_width": "wide",
            "dynamics_range": "moderate",
            "texture_type": "homophonic",
            "layers_count": 8,
            "density": "moderate"
        },
        "lyrics": {
            "theme": "overcoming challenges and personal growth",
            "key_phrases": ["rise above", "never give up", "find your way"],
            "symbolism": ["mountains as obstacles", "light as hope"],
            "prosody_quality": "excellent",
            "rhyme_scheme": "ABAB",
            "narrative_structure": "linear",
            "language": "English"
        },
        "arrangement": {
            "layers": ["verse stripped down", "chorus full band", "bridge breakdown"],
            "contrast_sections": ["verse vs chorus dynamics", "bridge texture change"],
            "effects_used": ["reverb", "delay", "chorus", "compression", "distortion"],
            "production_style": "standard",
            "sonic_signature": "modern pop-rock with layered vocals"
        },
        "mastering": {
            "loudness_lufs": -8.5,
            "peak_db": -0.3,
            "dynamic_range": 6.5,
            "eq_balance": "balanced",
            "stereo_imaging": "wide",
            "compression_level": "moderate"
        },
        "overall": {
            "emotional_arc": "Starts contemplative, builds energy through verses, explodes in chorus, reflective bridge, triumphant ending",
            "market_fit": "Contemporary pop-rock radio format, suitable for streaming playlists",
            "strengths": [
                "Strong hook in chorus",
                "Well-crafted build-ups",
                "Professional production quality",
                "Relatable lyrics",
                "Dynamic arrangement"
            ],
            "improvements": [
                "Bridge could be more distinctive",
                "Consider adding a pre-bridge transition",
                "Outro could be extended for radio fade",
                "Vocal harmonies in second chorus could be richer"
            ],
            "commercial_potential": "high",
            "artistic_merit": "high",
            "overall_rating": 8.2
        }
    }
    
    analyzer = MusicalAnalyzer()
    analyzer.analyze_from_dict(example_data)
    return analyzer


if __name__ == "__main__":
    # Create and display example analysis
    print("Creating example musical analysis...\n")
    analyzer = create_example_analysis()
    
    # Print the report
    print(analyzer.generate_report())
    
    # Also demonstrate JSON export
    print("\n\nJSON Export available via:")
    print("analyzer.get_complete_analysis()")
