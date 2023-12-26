# product list: ["cat", "banana", "obama", "car", "cow", "alibaba"].

root = {
    # C
    {
        "c": {
            # CA
            {
                "a": {
                    # CAT
                    {
                        "t": {},
                        "endWord": True
                    },
                    # CAR
                    {
                        "r": {},
                        "endWord": True
                    },
                    
                },
                "endWord": False
            },
            # CO
            {
                "o": {
                    # COW
                    {
                        "w": {},
                        "endWord": True
                    }
                },
                "endWord": False
            }
        },
        "endWord": False
    },
    # B
    {
        "b": {
            # BA
            {
                "a": {
                    # BAN
                    {
                        "n": {
                            # BANA
                            {
                                "a": {
                                    # BANAN
                                    {
                                        "n": {
                                            # BANANA
                                            {
                                                "a": {},
                                                "endWord": True
                                            }
                                        },
                                        "endWord": False
                                    }
                                },
                                "endWord": False
                            }
                        },
                        "endWord": False
                    }
                },
                "endWord": False
            }
        }
    },
    # O
    {
        "o": {
            # OB
            {
                "b": {
                    # OBA
                    {
                        "a": {
                            # OBAM
                            {
                                "m": {
                                    # OBAMA
                                    {
                                        "a": {},
                                        "endWord": True
                                    }
                                },
                                "endWord": False
                            }
                        },
                        "endWord": False
                    }
                },
                "endWord": False
            }
        },
        "endWord": False
    },
    # A
    {
        "a": {
            # AL
            {
                "l": {
                    # ALI
                    {
                        "i": {
                            # ALIB
                            {
                                "b": {
                                    # ALIBA
                                    {
                                        "a": {
                                            # ALIBAB
                                            {
                                                "b": {
                                                    # ALIBABA
                                                    {
                                                        "a": {},
                                                        "endWord": True
                                                    }
                                                },
                                                "endWord": False
                                            }
                                        },
                                        "endWord": False
                                    }
                                },
                                "endWord": False
                            }
                        },
                        "endWord": False
                    }
                },
                "endWord": False
            }
        },
        "endWord": False
    }
}