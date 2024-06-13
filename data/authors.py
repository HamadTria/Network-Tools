nodes = {
    "Author": ["Author 1", "Author 2", "Author 3"],
    "Paper": ["Paper 1", "Paper 2"],
    "Conference": ["Conf 1", "Conf 2"],
    "Book": ["Book 1", "Book 2"],
    "Institution": ["Institution 1", "Institution 2"],
    "Journal": ["Journal 1", "Journal 2"],
    "Publisher": ["Publisher 1", "Publisher 2"],
}

edges = [
    ("Author 1", "Paper 1"), ("Author 2", "Paper 1"),
    ("Author 2", "Paper 2"), ("Author 3", "Paper 2"),
    ("Author 1", "Conf 1"), ("Author 2", "Conf 1"),
    ("Author 3", "Conf 2"), 
    ("Author 1", "Book 1"), ("Author 3", "Book 1"),
    ("Author 2", "Book 2"), ("Author 3", "Book 2"),
    ("Author 1", "Institution 1"), ("Author 2", "Institution 1"),
    ("Author 2", "Institution 2"), ("Author 3", "Institution 2"),
    ("Author 1", "Journal 1"), ("Author 2", "Journal 1"),
    ("Author 2", "Journal 2"), ("Author 3", "Journal 2"),
    ("Author 1", "Publisher 1"), ("Author 2", "Publisher 1"),
    ("Author 2", "Publisher 2"), ("Author 3", "Publisher 2"),
]