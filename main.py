# Dictionary to store journal abbreviations and their full names
journal_dict = {
    'mt': 'ACS Applied Bio Materials',
    'el': 'ACS Applied Electronic Materials',
    'ae': 'ACS Applied Energy Materials',
    'am': 'ACS Applied Materials & Interfaces',
    'an': 'ACS Applied Nano Materials',
    'ap': 'ACS Applied Polymer Materials (ACS Admin)',
    'ab': 'ACS Biomaterials Science & Engineering',
    'cs': 'ACS Catalysis',
    'oc': 'ACS Central Science',
    'cb': 'ACS Chemical Biology',
    'cn': 'ACS Chemical Neuroscience',
    'co': 'ACS Combinatorial Sciences',
    'sp': 'ACS Earth and Space Chemistry',
    'nz': 'ACS Energy Letters',
    'id': 'ACS Infectious Diseases',
    'mz': 'ACS Macro Letters',
    'ml': 'ACS Medical Chemistry Letters',
    'nn': 'ACS Nano',
    'ao': 'ACS Omega',
    'pt': 'ACS Pharmacology & Translational Science',
    'ph': 'ACS Photonics',
    'sc': 'ACS Sustainable Chemistry & Engineering',
    'sb': 'ACS Synthetic Biology',
    'ar': 'Accounts of Chemical Research',
    'ac': 'Analytical Chemistry',
    'bi': 'Biochemistry',
    'bc': 'Bioconjugate Chemistry',
    'bm': 'Biomacromolecules',
    'tx': 'Chemical Research in Toxicology',
    'cr': 'Chemical Reviews',
    'cm': 'Chemistry of Materials',
    'cg': 'Crystal Growth & Design',
    'ef': 'Energy & Fuels',
    'es': 'Environmental Science & Technology',
    'ez': 'Environmental Science & Technology Letters',
    'ie': 'Industrial & Engineering Chemistry Research',
    'ic': 'Inorganic Chemistry',
    'jf': 'Journal of Agricultural and Food Chemistry',
    'je': 'Journal of Chemical & Engineering Data',
    'ed': 'Journal of Chemical Education',
    'ci': 'Journal of Chemical Information and Modeling',
    'ct': 'Journal of Chemical Theory and Computation',
    'cc': 'Journal of Combinatorial Chemistry',
    'jm': 'Journal of Medicinal Chemistry',
    'np': 'Journal of Natural Products',
    'pr': 'Journal of Proteome Research',
    'au': 'JACS Au',
    'ja': 'Journal of the American Chemical Society',
    'la': 'Langmuir',
    'ma': 'Macromolecules',
    'mp': 'Molecular Pharmaceutics',
    'nl': 'Nano Letters',
    'ol': 'Organic Letters',
    'op': 'Organic Process Research & Development',
    'om': 'Organometallics',
    'jo': 'The Journal of Organic Chemistry',
    'jp': 'The Journal of Physical Chemistry',
    'jz': 'The Journal of Physical Chemistry Letters'
    # You can add more abbreviations and full names here
}


def get_journal_full_name(abbreviation):
    # Convert abbreviation to lowercase to ensure case-insensitivity
    abbreviation = abbreviation.lower()
    # Look up the abbreviation in the dictionary
    return journal_dict.get(abbreviation, "Journal not found.")


def main():
    # User input for journal abbreviation
    user_input = input("Enter the journal abbreviation: ")
    # Get the full journal name
    full_name = get_journal_full_name(user_input)
    # Output the result
    print(full_name)


if __name__ == "__main__":
    main()
