DROP DATABASE IF EXISTS cahuilla;
CREATE DATABASE cahuilla;
ALTER DATABASE cahuilla CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use cahuilla;

CREATE TABLE morpheme (
    id INT NOT NULL AUTO_INCREMENT,
    canonicalForm VARCHAR(15),
    gloss VARCHAR(20),
    pos VARCHAR(5),
    PRIMARY KEY (id)
);

CREATE TABLE rootVerb (
    id INT NOT NULL,
    transitivity VARCHAR(15),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES morpheme(id)
);

CREATE TABLE nominalizer (
    id INT NOT NULL,
    class1Relationship VARCHAR(50),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES morpheme(id)
);

CREATE TABLE definition (
    id INT NOT NULL AUTO_INCREMENT,
    word_surface VARCHAR(200) NOT NULL,
    definition VARCHAR(200),
    PRIMARY KEY (id)
);


INSERT INTO morpheme
    (canonicalForm, gloss, pos)
VALUES
    ('at', 'NMLZ.ABST', 'SUFF'),
    ('ʔil̃', 'NMLZ.ABST', 'SUFF'),
    ('il̃', 'NMLZ.ABST', 'SUFF'),
    ('piš', 'NMLZ.FUT', 'SUFF'),
    ('vel', 'NMLZ.PFV', 'SUFF'),
    ('val', 'NMLZ.LOC', 'SUFF'),
    ('vúvan', 'to hit', 'verb'),
    ('kúp', 'to sleep', 'verb'),
    ('kʷáʔisni', 'to write', 'verb'),
    ('ʔámin', 'to throw', 'verb'),
    ('pívaʔ', 'to smoke', 'verb'),
    ('kúy', 'to bury', 'verb'),
    ('ʔásni', 'to bathe', 'verb'),
    ('yúmu', 'to put on the head', 'verb'),
    ('qáwi', 'to get tied', 'verb'),
    ('čeŋen', 'to dance', 'verb')
;

INSERT INTO rootVerb
    (id, transitivity)
VALUES
    ((SELECT id FROM morpheme WHERE canonicalForm = 'vúvan'), 'transitive'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'kúp'), 'intransitive'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'kʷáʔisni'), 'transitive'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'ʔámin'), 'transitive'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'pívaʔ'), 'intransitive'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'kúy'), 'transitive'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'ʔásni'), 'transitive'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'yúmu'), 'transitive'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'qáwi'), 'transitive'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'čeŋen'), 'transitive')
;

INSERT INTO nominalizer
    (id, class1Relationship)
VALUES
    ((SELECT id FROM morpheme WHERE canonicalForm = 'at'), 'verbal abstract noun'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'ʔil̃'), 'verbal abstract noun'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'il̃'), 'verbal abstract noun'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'piš'), 'event not yet occurred'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'vel'), 'already occurring or occurred'),
    ((SELECT id FROM morpheme WHERE canonicalForm = 'val'), 'location or place')
;

INSERT INTO definition
    (word_surface, definition)
VALUES
    ('ʔáminat', 'the throwing or the orphan'),
    ('kʷáʔisniat', 'the writing'),
    ('pívat', 'tobacco'),
    ('kʷáʔisniʔil̃', 'the writing'),
    ('kúyil̃', 'the burial'),
    ('ʔásniʔil̃', 'the bathing, the bath'),
    ('vúvanpiš', 'an insect that stings'),
    ('kúpvel', 'the bed'),
    ('yúmuvel', 'the hat'),
    ('qáwivel', 'handle'),
    ('čeŋenval', 'dancing place')
;

