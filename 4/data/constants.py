(pos,neutral,neg) = range(1,4)

NEGATION_WORDS = set(
                        [
                            "isn't", "isnt",
                            "wasn't", "wasnt",
                            "aren't", "arent",
                            "won't", "wont",
                            "can't", "cant",
                            "don't", "dont",
                            "no", "not"
                        ]
                    )

TOPTERMS_REGEX = '[A-Za-z0-9&\']+'
