from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary of journal abbreviations and names
journal_dict = {
    'mt': 'ACS Applied Bio Materials',
    'el': 'ACS Applied Electronic Materials',
    'ae': 'ACS Applied Energy Materials',
    'em': 'ACS Applied Engineering Materials',
    'am': 'ACS Applied Materials & Interfaces',
    'an': 'ACS Applied Nano Materials',
    'ot': 'ACS Applied Optical Materials',
    'ap': 'ACS Applied Polymer Materials',
    'bg': 'ACS Bio & Med Chem Au',
    'ab': 'ACS Biomaterials Science & Engineering',
    'cs': 'ACS Catalysis',
    'oc': 'ACS Central Science',
    'cb': 'ACS Chemical Biology',
    'hs': 'ACS Chemical Health & Safety',
    'cn': 'ACS Chemical Neuroscience',
    'co': 'ACS Combinatorial Sciences',
    'ea': 'ACS ES&T Air',
    'ew': 'ACS ES&T Water',
    'ee': 'ACS ES&T Engineering',
    'sp': 'ACS Earth and Space Chemistry',
    'ec': 'ACS Electrochemistry',
    'nz': 'ACS Energy Letters',
    'eg': 'ACS Engineering Au',
    'vg': 'ACS Environmental Au',
    'id': 'ACS Infectious Diseases',
    'mz': 'ACS Macro Letters',
    'mg': 'ACS Materials Au',
    'tz': 'ACS Materials Letters',
    'tg': 'ACS Measurement Science Au',
    'ml': 'ACS Medicinal Chemistry Letters',
    'nn': 'ACS Nano',
    'ng': 'ACS Nanoscience Au',
    'ao': 'ACS Omega',
    'gg': 'ACS Organic & Inorganic Au',
    'ph': 'ACS Photonics',
    'pg': 'ACS Physical Chemistry Au',
    'lg': 'ACS Polymers Au',
    'se': 'ACS Sensors',
    'sc': 'ACS Sustainable Chemistry & Engineering',
    'rm': 'ACS Sustainable Resource Management',
    'sb': 'ACS Synthetic Biology',
    'as': 'ACS Agricultural Science & Technology',
    'fs': 'ACS Food Science & Technology',
    'pt': 'ACS Pharmacology & Translational Science',
    'ar': 'Accounts of Chemical Research',
    'mr': 'Accounts of Materials Research',
    'ac': 'Analytical Chemistry',
    'af': 'Artificial Photosynthesis',
    'bi': 'Biochemistry',
    'bc': 'Bioconjugate Chemistry',
    'bm': 'Biomacromolecules',
    'be': 'Chem & Bio Engineering',
    'im': 'Chemical & Biomedical Imaging',
    'tx': 'Chemical Research in Toxicology',
    'cr': 'Chemical Reviews',
    'cm': 'Chemistry of Materials',
    'cg': 'Crystal Growth & Design',
    'ef': 'Energy & Fuels',
    'eh': 'Environment & Health',
    'es': 'Environmental Science & Technology',
    'ez': 'Environmental Science & Technology Letters',
    'ie': 'Industrial & Engineering Chemistry Research',
    'ic': 'Inorganic Chemistry',
    'au': 'JACS Au',
    'jf': 'Journal of Agricultural and Food Chemistry',
    'ed': 'Journal of Chemical Education',
    'ci': 'Journal of Chemical Information and Modeling',
    'ct': 'Journal of Chemical Theory and Computation',
    'je': 'Journal of Chemical & Engineering Data',
    'cc': 'Journal of Combinatorial Chemistry',
    'jm': 'Journal of Medicinal Chemistry',
    'np': 'Journal of Natural Products',
    'jp': 'The Journal of Physical Chemistry',
    'jz': 'The Journal of Physical Chemistry Letters',
    'pr': 'Journal of Proteome Research',
    'js': 'Journal of the American Society for Mass Spectrometry',
    'ja': 'Journal of the American Chemical Society',
    'la': 'Langmuir',
    'ma': 'Macromolecules',
    'mp': 'Molecular Pharmaceutics',
    'nl': 'Nano Letters',
    'ol': 'Organic Letters',
    'op': 'Organic Process Research & Development',
    'om': 'Organometallics',
    'pc': 'Precision Chemistry',
    'jo': 'The Journal of Organic Chemistry',
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lookup', methods=['POST'])
def lookup():
    abbreviation = request.json.get('abbreviation', '').lower()
    full_name = journal_dict.get(abbreviation, "Journal not found.")
    return jsonify({'full_name': full_name})


if __name__ == '__main__':
    app.run(debug=True)
