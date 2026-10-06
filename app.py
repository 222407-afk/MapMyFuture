import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="MapMyFuture",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SARVAM AI
# ============================================================

try:
    from sarvamai import SarvamAI
except ImportError:
    SarvamAI = None


def get_sarvam_response(prompt):

    if SarvamAI is None:
        return "Sarvam AI package is not installed."

    try:
        api_key = st.secrets["SARVAM_API_KEY"]

        client = SarvamAI(
            api_subscription_key=api_key
        )

        response = client.chat.completions(
            model="sarvam-105b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"Sarvam AI could not generate the response: {error}"


# ============================================================
# CAREER DATA
# ============================================================

CAREER_DATA = {

    "Technology & Computer Science": {
        "careers": [
            "Software Developer",
            "AI Engineer",
            "Data Scientist",
            "Cybersecurity Specialist",
            "App Developer"
        ],
        "subjects": [
            "Mathematics",
            "Computer Science",
            "Physics"
        ],
        "skills": [
            "Programming",
            "Logical Thinking",
            "Problem Solving",
            "Data Analysis",
            "Artificial Intelligence"
        ],
        "do": [
            "Learn programming fundamentals.",
            "Build apps and websites.",
            "Practice logical problem solving.",
            "Learn about artificial intelligence.",
            "Create projects for your portfolio.",
            "Learn APIs and databases.",
            "Keep improving your technical skills."
        ],
        "dont": [
            "Do not only memorise code.",
            "Do not copy projects without understanding them.",
            "Do not depend completely on AI.",
            "Do not ignore mathematics.",
            "Do not stop learning after one programming language."
        ],
        "universities": [
            "IIT Delhi",
            "IIT Bombay",
            "IIT Madras",
            "IIIT Hyderabad",
            "BITS Pilani"
        ],
        "abroad": [
            "MIT - USA",
            "Stanford University - USA",
            "Carnegie Mellon University - USA",
            "University of Oxford - UK",
            "University of Cambridge - UK",
            "University of Toronto - Canada"
        ]
    },

    "Engineering": {
        "careers": [
            "Mechanical Engineer",
            "Civil Engineer",
            "Electrical Engineer",
            "Robotics Engineer",
            "Aerospace Engineer"
        ],
        "subjects": [
            "Mathematics",
            "Physics",
            "Chemistry"
        ],
        "skills": [
            "Mathematics",
            "Physics",
            "Problem Solving",
            "Design Thinking",
            "Technical Skills"
        ],
        "do": [
            "Strengthen mathematics and physics.",
            "Build practical projects.",
            "Try robotics or electronics.",
            "Participate in engineering competitions.",
            "Develop problem-solving skills.",
            "Learn how engineering solves real problems."
        ],
        "dont": [
            "Do not focus only on memorising formulas.",
            "Do not avoid practical experiments.",
            "Do not choose engineering only because someone tells you to.",
            "Do not ignore communication skills.",
            "Do not assume all engineering branches are the same."
        ],
        "universities": [
            "IIT Delhi",
            "IIT Bombay",
            "IIT Kanpur",
            "IIT Kharagpur",
            "IIT Madras"
        ],
        "abroad": [
            "MIT - USA",
            "Stanford University - USA",
            "Caltech - USA",
            "University of Cambridge - UK",
            "Technical University of Munich - Germany",
            "University of Toronto - Canada"
        ]
    },

    "Medicine & Healthcare": {
        "careers": [
            "Doctor",
            "Dentist",
            "Pharmacist",
            "Physiotherapist",
            "Medical Researcher"
        ],
        "subjects": [
            "Biology",
            "Chemistry",
            "Physics"
        ],
        "skills": [
            "Biology",
            "Communication",
            "Empathy",
            "Scientific Thinking",
            "Consistency"
        ],
        "do": [
            "Build a strong foundation in biology.",
            "Study chemistry carefully.",
            "Develop consistent study habits.",
            "Learn about different healthcare careers.",
            "Develop communication and empathy.",
            "Understand education and entrance requirements."
        ],
        "dont": [
            "Do not choose medicine only because of reputation.",
            "Do not ignore the amount of study required.",
            "Do not assume doctor is the only healthcare career.",
            "Do not rely on social media for career decisions.",
            "Do not neglect your wellbeing."
        ],
        "universities": [
            "AIIMS New Delhi",
            "Christian Medical College, Vellore",
            "JIPMER, Puducherry",
            "Maulana Azad Medical College",
            "PGIMER Chandigarh"
        ],
        "abroad": [
            "Harvard University - USA",
            "Johns Hopkins University - USA",
            "University of Oxford - UK",
            "University of Cambridge - UK",
            "University of Melbourne - Australia",
            "University of Toronto - Canada"
        ]
    },

    "Business & Management": {
        "careers": [
            "Entrepreneur",
            "Business Analyst",
            "Marketing Manager",
            "Finance Professional",
            "Product Manager"
        ],
        "subjects": [
            "Economics",
            "Mathematics",
            "Business Studies"
        ],
        "skills": [
            "Leadership",
            "Communication",
            "Financial Literacy",
            "Marketing",
            "Decision Making"
        ],
        "do": [
            "Learn finance and economics.",
            "Develop communication skills.",
            "Develop leadership skills.",
            "Try entrepreneurship projects.",
            "Practice presentations.",
            "Learn how businesses solve customer problems."
        ],
        "dont": [
            "Do not think business is only about money.",
            "Do not ignore financial literacy.",
            "Do not make decisions without research.",
            "Do not be afraid to learn from mistakes.",
            "Do not assume entrepreneurship is easy."
        ],
        "universities": [
            "IIM Ahmedabad",
            "IIM Bangalore",
            "IIM Calcutta",
            "IIM Lucknow",
            "IIM Kozhikode"
        ],
        "abroad": [
            "Wharton - USA",
            "Harvard University - USA",
            "New York University - USA",
            "London School of Economics - UK",
            "University of Oxford - UK",
            "National University of Singapore - Singapore"
        ]
    },

    "Law & Public Service": {
        "careers": [
            "Lawyer",
            "Civil Servant",
            "Policy Analyst",
            "Legal Researcher",
            "Public Administrator"
        ],
        "subjects": [
            "English",
            "Social Science",
            "Political Science",
            "Economics"
        ],
        "skills": [
            "Communication",
            "Public Speaking",
            "Research",
            "Critical Thinking",
            "Writing"
        ],
        "do": [
            "Improve reading and writing.",
            "Follow current events.",
            "Practice debating.",
            "Practice public speaking.",
            "Learn how laws and governments work.",
            "Develop research skills."
        ],
        "dont": [
            "Do not rely only on memorisation.",
            "Do not ignore evidence.",
            "Do not avoid different viewpoints.",
            "Do not assume confidence is enough.",
            "Do not ignore communication skills."
        ],
        "universities": [
            "National Law School of India University",
            "National Law University Delhi",
            "NALSAR University of Law",
            "National Law University Jodhpur",
            "Symbiosis Law School"
        ],
        "abroad": [
            "Harvard Law School - USA",
            "Yale Law School - USA",
            "Stanford Law School - USA",
            "University of Oxford - UK",
            "University of Cambridge - UK",
            "University of Melbourne - Australia"
        ]
    },

    "Science & Research": {
        "careers": [
            "Research Scientist",
            "Biotechnologist",
            "Physicist",
            "Chemist",
            "Environmental Scientist"
        ],
        "subjects": [
            "Physics",
            "Chemistry",
            "Biology",
            "Mathematics"
        ],
        "skills": [
            "Scientific Thinking",
            "Research",
            "Data Analysis",
            "Mathematics",
            "Experimentation"
        ],
        "do": [
            "Ask questions.",
            "Investigate how things work.",
            "Practice scientific reasoning.",
            "Learn data analysis.",
            "Participate in science fairs.",
            "Try research projects."
        ],
        "dont": [
            "Do not accept information without checking evidence.",
            "Do not be afraid of mathematics.",
            "Do not treat one experiment as absolute proof.",
            "Do not avoid data analysis.",
            "Do not assume research only happens in laboratories."
        ],
        "universities": [
            "Indian Institute of Science",
            "IISER Pune",
            "IISER Kolkata",
            "IISER Mohali",
            "IIT Delhi"
        ],
        "abroad": [
            "MIT - USA",
            "Caltech - USA",
            "Stanford University - USA",
            "University of Oxford - UK",
            "University of Cambridge - UK",
            "Technical University of Munich - Germany"
        ]
    },

    "Design & Creative Arts": {
        "careers": [
            "Graphic Designer",
            "UI/UX Designer",
            "Animator",
            "Architect",
            "Video Creator"
        ],
        "subjects": [
            "Art",
            "Design",
            "Computer Science",
            "Mathematics"
        ],
        "skills": [
            "Creativity",
            "Visual Design",
            "UI/UX",
            "Communication",
            "Digital Tools"
        ],
        "do": [
            "Build a portfolio.",
            "Learn design principles.",
            "Experiment with digital design tools.",
            "Study user experience.",
            "Practice explaining design decisions.",
            "Combine creative and technical skills."
        ],
        "dont": [
            "Do not copy other people's work.",
            "Do not ignore feedback.",
            "Do not stop practising.",
            "Do not ignore technical skills.",
            "Do not underestimate communication skills."
        ],
        "universities": [
            "National Institute of Design",
            "IIT Bombay IDC School of Design",
            "National Institute of Fashion Technology",
            "Srishti Manipal Institute",
            "MIT Institute of Design"
        ],
        "abroad": [
            "Rhode Island School of Design - USA",
            "Parsons School of Design - USA",
            "Pratt Institute - USA",
            "Royal College of Art - UK",
            "University of the Arts London - UK",
            "RMIT University - Australia"
        ]
    }
}


# ============================================================
# SUBJECT QUESTION BANK
# ============================================================

SUBJECT_QUESTIONS = {

    "Mathematics": {
        "question": "What is 12 × 8?",
        "options": ["86", "96", "108", "112"],
        "answer": "96"
    },

    "Physics": {
        "question": "Which unit is commonly used to measure force?",
        "options": ["Joule", "Newton", "Watt", "Pascal"],
        "answer": "Newton"
    },

    "Chemistry": {
        "question": "What is the chemical symbol for oxygen?",
        "options": ["Ox", "O", "Og", "C"],
        "answer": "O"
    },

    "Biology": {
        "question": "Which organ pumps blood around the human body?",
        "options": ["Lungs", "Brain", "Heart", "Kidney"],
        "answer": "Heart"
    },

    "Computer Science": {
        "question": "Which of these is a programming language?",
        "options": ["Python", "Chrome", "Windows", "Google"],
        "answer": "Python"
    },

    "English": {
        "question": "Which word is a noun?",
        "options": ["Quickly", "Beautiful", "School", "Run"],
        "answer": "School"
    },

    "Social Science": {
        "question": "Which branch studies human societies and social relationships?",
        "options": [
            "Sociology",
            "Astronomy",
            "Botany",
            "Geology"
        ],
        "answer": "Sociology"
    },

    "Economics": {
        "question": "What does GDP broadly measure?",
        "options": [
            "A country's total economic output",
            "A country's population only",
            "The number of schools",
            "The country's land area"
        ],
        "answer": "A country's total economic output"
    },

    "Art": {
        "question": "Which element is commonly used to describe how light or dark a colour appears?",
        "options": [
            "Value",
            "Temperature",
            "Perspective",
            "Texture"
        ],
        "answer": "Value"
    },

    "Business Studies": {
        "question": "What is a person who starts and manages a business commonly called?",
        "options": [
            "Entrepreneur",
            "Astronomer",
            "Biologist",
            "Geologist"
        ],
        "answer": "Entrepreneur"
    },

    "Political Science": {
        "question": "What is the study of government and political systems called?",
        "options": [
            "Political Science",
            "Biology",
            "Chemistry",
            "Geometry"
        ],
        "answer": "Political Science"
    }
}


# ============================================================
# CAREER MAP DATA
# ============================================================

CAREER_MAP = {

    "Technology & Computer Science": {
        "start": "Your Interests",
        "step1": "Mathematics + Computer Science",
        "step2": "Programming + Logic + Problem Solving",
        "step3": "Technology & Computer Science",
        "step4": "Software Developer / AI Engineer / Data Scientist",
        "step5": "Build Projects + Learn Advanced Skills",
        "finish": "University → Internship → Career"
    },

    "Engineering": {
        "start": "Your Interests",
        "step1": "Mathematics + Physics",
        "step2": "Problem Solving + Design Thinking",
        "step3": "Engineering",
        "step4": "Robotics / Civil / Mechanical / Electrical",
        "step5": "Projects + Competitions + Technical Skills",
        "finish": "University → Internship → Engineering Career"
    },

    "Medicine & Healthcare": {
        "start": "Your Interests",
        "step1": "Biology + Chemistry + Physics",
        "step2": "Scientific Thinking + Communication",
        "step3": "Medicine & Healthcare",
        "step4": "Doctor / Dentist / Pharmacist / Researcher",
        "step5": "Entrance Preparation + Healthcare Experience",
        "finish": "Medical Education → Training → Healthcare Career"
    },

    "Business & Management": {
        "start": "Your Interests",
        "step1": "Economics + Business + Mathematics",
        "step2": "Leadership + Communication + Finance",
        "step3": "Business & Management",
        "step4": "Entrepreneur / Analyst / Marketing / Finance",
        "step5": "Business Projects + Internships + Leadership",
        "finish": "University → Experience → Business Career"
    },

    "Law & Public Service": {
        "start": "Your Interests",
        "step1": "English + Social Science + Political Science",
        "step2": "Communication + Research + Critical Thinking",
        "step3": "Law & Public Service",
        "step4": "Lawyer / Policy Analyst / Civil Servant",
        "step5": "Reading + Debate + Public Speaking",
        "finish": "University → Training → Public/Legal Career"
    },

    "Science & Research": {
        "start": "Your Interests",
        "step1": "Physics + Chemistry + Biology + Mathematics",
        "step2": "Research + Experimentation + Data Analysis",
        "step3": "Science & Research",
        "step4": "Scientist / Biotechnologist / Physicist",
        "step5": "Research Projects + Science Competitions",
        "finish": "University → Research → Specialisation"
    },

    "Design & Creative Arts": {
        "start": "Your Interests",
        "step1": "Art + Design + Technology",
        "step2": "Creativity + Visual Thinking + UI/UX",
        "step3": "Design & Creative Arts",
        "step4": "Designer / Animator / Architect / UI/UX",
        "step5": "Portfolio + Design Projects + Feedback",
        "finish": "University → Portfolio → Creative Career"
    }
}


# ============================================================
# HEADER
# ============================================================

st.title("🧭 MapMyFuture")

st.subheader(
    "Discover your strengths. Explore careers. Plan your future."
)

st.write(
    "A career exploration assessment designed to help students "
    "understand their interests, strengths and possible career paths."
)

st.divider()


# ============================================================
# FOCUS MODE
# ============================================================

st.warning(
    "🔒 Focus Mode: Please stay on this quiz page while answering. "
    "MapMyFuture can detect when the browser page becomes hidden, "
    "but a normal Streamlit website cannot physically lock Chrome "
    "tabs or prevent Alt+Tab."
)

components.html(
    """
    <script>
    document.addEventListener("visibilitychange", function() {
        if (document.hidden) {
            console.log("MapMyFuture: student left the quiz page.");
        }
    });
    </script>
    """,
    height=1
)


# ============================================================
# QUIZ
# ============================================================

st.header("🧠 Career Discovery Assessment")

st.write(
    "This assessment contains 25 main questions, including "
    "3 fill-in-the-blank questions."
)

st.info(
    "Answer honestly. There are no perfect answers. "
    "Your result is a starting point for career exploration."
)


with st.form("career_quiz"):

    student_name = st.text_input(
        "👤 Student Name",
        placeholder="Enter your full name"
    )

    st.divider()

    # Q1
    st.subheader("1. Which activities do you enjoy most?")

    q1 = st.multiselect(
        "Select up to 4.",
        [
            "Solving maths or logic problems",
            "Using computers and technology",
            "Helping people",
            "Creating art or designs",
            "Reading and writing",
            "Doing experiments",
            "Managing money or business",
            "Building or repairing things"
        ],
        max_selections=4
    )

    # Q2
    st.subheader("2. Which subjects do you enjoy?")

    q2 = st.multiselect(
        "Select all subjects you genuinely enjoy.",
        [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology",
            "Computer Science",
            "English",
            "Social Science",
            "Economics",
            "Business Studies",
            "Political Science",
            "Art"
        ]
    )

    # Q3
    st.subheader("3. What type of work sounds most interesting?")

    q3 = st.radio(
        "Choose one.",
        [
            "Working with computers and technology",
            "Working with people",
            "Running a business",
            "Researching and discovering things",
            "Creating and designing",
            "Solving engineering problems",
            "Law, government or public service"
        ]
    )

    # Q4
    st.subheader("4. How do you usually solve a difficult problem?")

    q4 = st.radio(
        "Choose one.",
        [
            "Break it into smaller logical steps",
            "Research before deciding",
            "Ask people and work as a team",
            "Try creative solutions",
            "Experiment until something works"
        ]
    )

    # Q5
    st.subheader("5. Which skill would you most like to develop?")

    q5 = st.radio(
        "Choose one.",
        [
            "Programming",
            "Communication",
            "Leadership",
            "Creativity",
            "Scientific thinking",
            "Business skills",
            "Problem solving"
        ]
    )

    # Q6
    st.subheader("6. Which workplace sounds most interesting?")

    q6 = st.radio(
        "Choose one.",
        [
            "Technology company",
            "Hospital or healthcare environment",
            "Laboratory or research centre",
            "Business office",
            "Court or government organisation",
            "Creative studio",
            "Engineering workshop"
        ]
    )

    # Q7
    st.subheader("7. How do you feel about teamwork?")

    q7 = st.radio(
        "Choose one.",
        [
            "I love teamwork",
            "I like both teamwork and individual work",
            "I prefer independent work"
        ]
    )

    # Q8
    st.subheader("8. What motivates you most?")

    q8 = st.radio(
        "Choose one.",
        [
            "Creating new technology",
            "Helping people",
            "Discovering knowledge",
            "Building a business",
            "Creating something unique",
            "Solving difficult problems",
            "Making a positive social impact"
        ]
    )

    # Q9
    st.subheader("9. Which activity would you choose for a free afternoon?")

    q9 = st.radio(
        "Choose one.",
        [
            "Build an app",
            "Do a science experiment",
            "Design something",
            "Help someone learn",
            "Plan a small business idea",
            "Debate an important topic"
        ]
    )

    # Q10
    st.subheader("10. Which type of challenge do you enjoy?")

    q10 = st.radio(
        "Choose one.",
        [
            "Technical challenge",
            "Scientific challenge",
            "Creative challenge",
            "People-focused challenge",
            "Business challenge",
            "Social or legal challenge"
        ]
    )

    # Q11
    st.subheader("11. What are you usually good at?")

    q11 = st.radio(
        "Choose one.",
        [
            "Logical thinking",
            "Explaining ideas",
            "Remembering scientific information",
            "Creating things",
            "Organising people",
            "Writing arguments"
        ]
    )

    # Q12
    st.subheader("12. Which project would you most enjoy?")

    q12 = st.radio(
        "Choose one.",
        [
            "Creating a mobile app",
            "Building a robot",
            "Researching a scientific question",
            "Creating a poster or animation",
            "Starting a small business",
            "Researching a social issue"
        ]
    )

    # Q13
    st.subheader("13. How comfortable are you with mathematics?")

    q13 = st.radio(
        "Choose one.",
        [
            "I really enjoy mathematics",
            "I am comfortable with mathematics",
            "I am okay with mathematics",
            "I do not enjoy mathematics much"
        ]
    )

    # Q14
    st.subheader("14. How comfortable are you with science?")

    q14 = st.radio(
        "Choose one.",
        [
            "I really enjoy science",
            "I am comfortable with science",
            "I like some areas of science",
            "Science is not my favourite"
        ]
    )

    # Q15
    st.subheader("15. How comfortable are you with technology?")

    q15 = st.radio(
        "Choose one.",
        [
            "I love technology",
            "I enjoy using technology",
            "I can use technology when needed",
            "I prefer non-technical activities"
        ]
    )

    # Q16
    st.subheader("16. Which role would you prefer in a team?")

    q16 = st.radio(
        "Choose one.",
        [
            "Technical problem solver",
            "Team leader",
            "Researcher",
            "Designer",
            "Presenter",
            "Planner"
        ]
    )

    # Q17
    st.subheader("17. What type of result makes you happiest?")

    q17 = st.radio(
        "Choose one.",
        [
            "A working program",
            "A successful experiment",
            "A creative design",
            "Helping someone",
            "A successful business idea",
            "A strong argument"
        ]
    )

    # Q18
    st.subheader("18. Which skill would you like people to recognise you for?")

    q18 = st.radio(
        "Choose one.",
        [
            "Technical ability",
            "Scientific knowledge",
            "Creativity",
            "Leadership",
            "Communication",
            "Problem solving"
        ]
    )

    # Q19
    st.subheader("19. What type of learning do you prefer?")

    q19 = st.radio(
        "Choose one.",
        [
            "Learning by coding",
            "Learning through experiments",
            "Learning through reading",
            "Learning by designing",
            "Learning through discussions",
            "Learning by doing projects"
        ]
    )

    # Q20
    st.subheader("20. What would you most like to improve?")

    q20 = st.radio(
        "Choose one.",
        [
            "Programming",
            "Mathematics",
            "Scientific knowledge",
            "Communication",
            "Creativity",
            "Leadership"
        ]
    )

    # Q21
    st.subheader("21. Which future sounds most exciting?")

    q21 = st.radio(
        "Choose one.",
        [
            "Building advanced technology",
            "Discovering something new",
            "Helping people through healthcare",
            "Running a company",
            "Designing creative products",
            "Working in law or government"
        ]
    )

    # Q22
    st.subheader("22. How do you react when your first idea fails?")

    q22 = st.radio(
        "Choose one.",
        [
            "Debug it and try again",
            "Research why it failed",
            "Ask others for ideas",
            "Create a completely different approach",
            "Analyse the business or practical problem"
        ]
    )

    # Q23
    st.subheader("23. Fill in the blank")

    st.write(
        "The language commonly used to create Streamlit applications is ______."
    )

    q23 = st.text_input(
        "Your answer:",
        key="fill_1"
    )

    # Q24
    st.subheader("24. Fill in the blank")

    st.write(
        "The branch of science that studies living organisms is ______."
    )

    q24 = st.text_input(
        "Your answer:",
        key="fill_2"
    )

    # Q25
    st.subheader("25. Fill in the blank")

    st.write(
        "A person who starts and manages a business is commonly called an ______."
    )

    q25 = st.text_input(
        "Your answer:",
        key="fill_3"
    )

    # ========================================================
    # SUBJECT QUESTIONS
    # ========================================================

    st.divider()

    st.header("📚 Subject Knowledge Check")

    st.write(
        "You selected these subjects as subjects you enjoy. "
        "You will get one short question for each selected subject."
    )

    selected_subject_questions = []

    for subject in q2:

        if subject in SUBJECT_QUESTIONS:

            data = SUBJECT_QUESTIONS[subject]

            st.subheader(f"📘 {subject}")

            answer = st.radio(
                data["question"],
                data["options"],
                key=f"subject_{subject}"
            )

            selected_subject_questions.append(
                {
                    "subject": subject,
                    "answer": answer,
                    "correct": data["answer"]
                }
            )

    st.divider()

    st.caption(
        "Before submitting, check that you have answered every question."
    )

    submitted = st.form_submit_button(
        "🚀 Submit My Career Assessment"
    )


# ============================================================
# PROCESS RESULTS
# ============================================================

if submitted:

    if not student_name.strip():
        st.error(
            "Please enter your name before submitting the assessment."
        )
        st.stop()

    scores = {
        "Technology & Computer Science": 0,
        "Engineering": 0,
        "Medicine & Healthcare": 0,
        "Business & Management": 0,
        "Law & Public Service": 0,
        "Science & Research": 0,
        "Design & Creative Arts": 0
    }

    # ========================================================
    # Q1
    # ========================================================

    for answer in q1:

        if answer == "Solving maths or logic problems":
            scores["Technology & Computer Science"] += 2
            scores["Engineering"] += 2

        elif answer == "Using computers and technology":
            scores["Technology & Computer Science"] += 3

        elif answer == "Helping people":
            scores["Medicine & Healthcare"] += 3

        elif answer == "Creating art or designs":
            scores["Design & Creative Arts"] += 3

        elif answer == "Reading and writing":
            scores["Law & Public Service"] += 2

        elif answer == "Doing experiments":
            scores["Science & Research"] += 3

        elif answer == "Managing money or business":
            scores["Business & Management"] += 3

        elif answer == "Building or repairing things":
            scores["Engineering"] += 3

    # ========================================================
    # Q2
    # ========================================================

    for subject in q2:

        if subject == "Mathematics":
            scores["Technology & Computer Science"] += 2
            scores["Engineering"] += 2

        elif subject == "Physics":
            scores["Engineering"] += 2
            scores["Science & Research"] += 2

        elif subject == "Chemistry":
            scores["Medicine & Healthcare"] += 2
            scores["Science & Research"] += 2

        elif subject == "Biology":
            scores["Medicine & Healthcare"] += 3
            scores["Science & Research"] += 2

        elif subject == "Computer Science":
            scores["Technology & Computer Science"] += 3

        elif subject == "English":
            scores["Law & Public Service"] += 2

        elif subject == "Social Science":
            scores["Law & Public Service"] += 2

        elif subject == "Economics":
            scores["Business & Management"] += 3

        elif subject == "Business Studies":
            scores["Business & Management"] += 3

        elif subject == "Political Science":
            scores["Law & Public Service"] += 3

        elif subject == "Art":
            scores["Design & Creative Arts"] += 3

    # ========================================================
    # Q3
    # ========================================================

    q3_map = {
        "Working with computers and technology":
            "Technology & Computer Science",
        "Working with people":
            "Medicine & Healthcare",
        "Running a business":
            "Business & Management",
        "Researching and discovering things":
            "Science & Research",
        "Creating and designing":
            "Design & Creative Arts",
        "Solving engineering problems":
            "Engineering",
        "Law, government or public service":
            "Law & Public Service"
    }

    scores[q3_map[q3]] += 4

    # ========================================================
    # Q4
    # ========================================================

    if q4 == "Break it into smaller logical steps":
        scores["Technology & Computer Science"] += 2
        scores["Engineering"] += 2

    elif q4 == "Research before deciding":
        scores["Science & Research"] += 3

    elif q4 == "Ask people and work as a team":
        scores["Medicine & Healthcare"] += 2
        scores["Business & Management"] += 2

    elif q4 == "Try creative solutions":
        scores["Design & Creative Arts"] += 3

    elif q4 == "Experiment until something works":
        scores["Engineering"] += 2
        scores["Science & Research"] += 2

    # ========================================================
    # Q5
    # ========================================================

    skill_map = {
        "Programming": "Technology & Computer Science",
        "Communication": "Law & Public Service",
        "Leadership": "Business & Management",
        "Creativity": "Design & Creative Arts",
        "Scientific thinking": "Science & Research",
        "Business skills": "Business & Management",
        "Problem solving": "Engineering"
    }

    scores[skill_map[q5]] += 3

    # ========================================================
    # Q6
    # ========================================================

    workplace_map = {
        "Technology company": "Technology & Computer Science",
        "Hospital or healthcare environment": "Medicine & Healthcare",
        "Laboratory or research centre": "Science & Research",
        "Business office": "Business & Management",
        "Court or government organisation": "Law & Public Service",
        "Creative studio": "Design & Creative Arts",
        "Engineering workshop": "Engineering"
    }

    scores[workplace_map[q6]] += 3

    # ========================================================
    # Q7
    # ========================================================

    if q7 == "I love teamwork":
        scores["Business & Management"] += 2
        scores["Medicine & Healthcare"] += 1

    elif q7 == "I like both teamwork and individual work":
        scores["Technology & Computer Science"] += 1
        scores["Business & Management"] += 1

    else:
        scores["Technology & Computer Science"] += 2
        scores["Science & Research"] += 1

    # ========================================================
    # Q8
    # ========================================================

    motivation_map = {
        "Creating new technology": "Technology & Computer Science",
        "Helping people": "Medicine & Healthcare",
        "Discovering knowledge": "Science & Research",
        "Building a business": "Business & Management",
        "Creating something unique": "Design & Creative Arts",
        "Solving difficult problems": "Engineering",
        "Making a positive social impact": "Law & Public Service"
    }

    scores[motivation_map[q8]] += 3

    # ========================================================
    # Q9
    # ========================================================

    q9_map = {
        "Build an app": "Technology & Computer Science",
        "Do a science experiment": "Science & Research",
        "Design something": "Design & Creative Arts",
        "Help someone learn": "Medicine & Healthcare",
        "Plan a small business idea": "Business & Management",
        "Debate an important topic": "Law & Public Service"
    }

    scores[q9_map[q9]] += 2

    # ========================================================
    # Q10
    # ========================================================

    q10_map = {
        "Technical challenge": "Technology & Computer Science",
        "Scientific challenge": "Science & Research",
        "Creative challenge": "Design & Creative Arts",
        "People-focused challenge": "Medicine & Healthcare",
        "Business challenge": "Business & Management",
        "Social or legal challenge": "Law & Public Service"
    }

    scores[q10_map[q10]] += 2

    # ========================================================
    # Q11
    # ========================================================

    q11_map = {
        "Logical thinking": "Technology & Computer Science",
        "Explaining ideas": "Law & Public Service",
        "Remembering scientific information": "Science & Research",
        "Creating things": "Design & Creative Arts",
        "Organising people": "Business & Management",
        "Writing arguments": "Law & Public Service"
    }

    scores[q11_map[q11]] += 2

    # ========================================================
    # Q12
    # ========================================================

    q12_map = {
        "Creating a mobile app": "Technology & Computer Science",
        "Building a robot": "Engineering",
        "Researching a scientific question": "Science & Research",
        "Creating a poster or animation": "Design & Creative Arts",
        "Starting a small business": "Business & Management",
        "Researching a social issue": "Law & Public Service"
    }

    scores[q12_map[q12]] += 2

    # ========================================================
    # Q13
    # ========================================================

    if q13 == "I really enjoy mathematics":
        scores["Technology & Computer Science"] += 2
        scores["Engineering"] += 2
        scores["Science & Research"] += 1

    elif q13 == "I am comfortable with mathematics":
        scores["Engineering"] += 1
        scores["Technology & Computer Science"] += 1

    # ========================================================
    # Q14
    # ========================================================

    if q14 == "I really enjoy science":
        scores["Science & Research"] += 2
        scores["Medicine & Healthcare"] += 2
        scores["Engineering"] += 1

    elif q14 == "I am comfortable with science":
        scores["Science & Research"] += 1
        scores["Engineering"] += 1

    # ========================================================
    # Q15
    # ========================================================

    if q15 == "I love technology":
        scores["Technology & Computer Science"] += 3

    elif q15 == "I enjoy using technology":
        scores["Technology & Computer Science"] += 2

    elif q15 == "I can use technology when needed":
        scores["Technology & Computer Science"] += 1

    # ========================================================
    # Q16
    # ========================================================

    q16_map = {
        "Technical problem solver": "Technology & Computer Science",
        "Team leader": "Business & Management",
        "Researcher": "Science & Research",
        "Designer": "Design & Creative Arts",
        "Presenter": "Law & Public Service",
        "Planner": "Engineering"
    }

    scores[q16_map[q16]] += 2

    # ========================================================
    # Q17
    # ========================================================

    q17_map = {
        "A working program": "Technology & Computer Science",
        "A successful experiment": "Science & Research",
        "A creative design": "Design & Creative Arts",
        "Helping someone": "Medicine & Healthcare",
        "A successful business idea": "Business & Management",
        "A strong argument": "Law & Public Service"
    }

    scores[q17_map[q17]] += 2

    # ========================================================
    # Q18
    # ========================================================

    q18_map = {
        "Technical ability": "Technology & Computer Science",
        "Scientific knowledge": "Science & Research",
        "Creativity": "Design & Creative Arts",
        "Leadership": "Business & Management",
        "Communication": "Law & Public Service",
        "Problem solving": "Engineering"
    }

    scores[q18_map[q18]] += 2

    # ========================================================
    # Q19
    # ========================================================

    q19_map = {
        "Learning by coding": "Technology & Computer Science",
        "Learning through experiments": "Science & Research",
        "Learning through reading": "Law & Public Service",
        "Learning by designing": "Design & Creative Arts",
        "Learning through discussions": "Business & Management",
        "Learning by doing projects": "Engineering"
    }

    scores[q19_map[q19]] += 2

    # ========================================================
    # Q20
    # ========================================================

    q20_map = {
        "Programming": "Technology & Computer Science",
        "Mathematics": "Engineering",
        "Scientific knowledge": "Science & Research",
        "Communication": "Law & Public Service",
        "Creativity": "Design & Creative Arts",
        "Leadership": "Business & Management"
    }

    scores[q20_map[q20]] += 2

    # ========================================================
    # Q21
    # ========================================================

    q21_map = {
        "Building advanced technology": "Technology & Computer Science",
        "Discovering something new": "Science & Research",
        "Helping people through healthcare": "Medicine & Healthcare",
        "Running a company": "Business & Management",
        "Designing creative products": "Design & Creative Arts",
        "Working in law or government": "Law & Public Service"
    }

    scores[q21_map[q21]] += 3

    # ========================================================
    # Q22
    # ========================================================

    if q22 == "Debug it and try again":
        scores["Technology & Computer Science"] += 2
        scores["Engineering"] += 1

    elif q22 == "Research why it failed":
        scores["Science & Research"] += 2

    elif q22 == "Ask others for ideas":
        scores["Business & Management"] += 1
        scores["Medicine & Healthcare"] += 1

    elif q22 == "Create a completely different approach":
        scores["Design & Creative Arts"] += 2

    elif q22 == "Analyse the business or practical problem":
        scores["Business & Management"] += 2
        scores["Engineering"] += 1

    # ========================================================
    # Q23
    # ========================================================

    if q23.strip().lower() in [
        "python",
        "python programming",
        "python language"
    ]:
        scores["Technology & Computer Science"] += 3

    # ========================================================
    # Q24
    # ========================================================

    if q24.strip().lower() in [
        "biology",
        "biological science"
    ]:
        scores["Science & Research"] += 3
        scores["Medicine & Healthcare"] += 1

    # ========================================================
    # Q25
    # ========================================================

    if q25.strip().lower().replace(".", "") == "entrepreneur":
        scores["Business & Management"] += 3

    # ========================================================
    # SUBJECT SCORING
    # ========================================================

    subject_results = []

    for item in selected_subject_questions:

        subject = item["subject"]
        answer = item["answer"]
        correct = item["correct"]

        is_correct = answer == correct

        subject_results.append(
            {
                "subject": subject,
                "answer": answer,
                "correct": correct,
                "is_correct": is_correct
            }
        )

        if is_correct:

            if subject in [
                "Mathematics",
                "Computer Science"
            ]:
                scores["Technology & Computer Science"] += 2

            if subject in [
                "Mathematics",
                "Physics"
            ]:
                scores["Engineering"] += 2

            if subject in [
                "Biology",
                "Chemistry"
            ]:
                scores["Medicine & Healthcare"] += 2

            if subject in [
                "Physics",
                "Chemistry",
                "Biology",
                "Mathematics"
            ]:
                scores["Science & Research"] += 2

            if subject in [
                "English",
                "Social Science",
                "Political Science"
            ]:
                scores["Law & Public Service"] += 2

            if subject in [
                "Economics",
                "Business Studies"
            ]:
                scores["Business & Management"] += 2

            if subject == "Art":
                scores["Design & Creative Arts"] += 2

    # ========================================================
    # SORT RESULTS
    # ========================================================

    sorted_scores = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    top_career = sorted_scores[0][0]
    top_score = sorted_scores[0][1]
    second_career = sorted_scores[1][0]

    career = CAREER_DATA[top_career]

    # ========================================================
    # RESULT HEADER
    # ========================================================

    st.divider()

    st.header(
        f"🎯 {student_name.strip()}'s MapMyFuture Result"
    )

    st.success(
        f"Hello {student_name.strip()}! "
        f"Your strongest career direction is {top_career}."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Career Match Score",
            str(top_score)
        )

    with col2:
        st.metric(
            "Second Strongest Area",
            second_career
        )

    # ========================================================
    # CAREER MAP
    # ========================================================

    st.divider()

    st.header("🗺️ Your Career Map")

    st.write(
        "This map shows one possible path from your current "
        "interests to careers you can explore."
    )

    career_map = CAREER_MAP[top_career]

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:15px;
            border:2px solid #4F8BF9;
            background-color:#F7FAFF;
            margin-bottom:10px;
        ">
            <h3>🧑‍🎓 {career_map["start"]}</h3>
            <p style="font-size:18px;">Your quiz answers</p>
        </div>

        <div style="text-align:center;font-size:30px;">
            ↓
        </div>

        <div style="
            padding:20px;
            border-radius:15px;
            border:2px solid #6C63FF;
            margin-bottom:10px;
        ">
            <h3>📚 Step 1: Subjects</h3>
            <p style="font-size:18px;">{career_map["step1"]}</p>
        </div>

        <div style="text-align:center;font-size:30px;">
            ↓
        </div>

        <div style="
            padding:20px;
            border-radius:15px;
            border:2px solid #00A878;
            margin-bottom:10px;
        ">
            <h3>🧠 Step 2: Skills</h3>
            <p style="font-size:18px;">{career_map["step2"]}</p>
        </div>

        <div style="text-align:center;font-size:30px;">
            ↓
        </div>

        <div style="
            padding:20px;
            border-radius:15px;
            border:2px solid #F39C12;
            margin-bottom:10px;
        ">
            <h3>🎯 Step 3: Career Area</h3>
            <p style="font-size:20px;"><b>{career_map["step3"]}</b></p>
        </div>

        <div style="text-align:center;font-size:30px;">
            ↓
        </div>

        <div style="
            padding:20px;
            border-radius:15px;
            border:2px solid #E74C3C;
            margin-bottom:10px;
        ">
            <h3>💼 Step 4: Careers</h3>
            <p style="font-size:18px;">{career_map["step4"]}</p>
        </div>

        <div style="text-align:center;font-size:30px;">
            ↓
        </div>

        <div style="
            padding:20px;
            border-radius:15px;
            border:2px solid #9B59B6;
            margin-bottom:10px;
        ">
            <h3>🚀 Step 5: Preparation</h3>
            <p style="font-size:18px;">{career_map["step5"]}</p>
        </div>

        <div style="text-align:center;font-size:30px;">
            ↓
        </div>

        <div style="
            padding:20px;
            border-radius:15px;
            border:2px solid #2C3E50;
            background-color:#F7FAFC;
        ">
            <h3>🏆 Your Possible Next Stage</h3>
            <p style="font-size:18px;">{career_map["finish"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # SKILLS
    # ========================================================

    st.subheader("🧠 Skills to Build")

    skill_columns = st.columns(3)

    for index, skill in enumerate(career["skills"]):

        with skill_columns[index % 3]:
            st.info(f"⭐ {skill}")

    # ========================================================
    # CAREER OPTIONS
    # ========================================================

    st.subheader("💼 Careers You Could Explore")

    columns = st.columns(3)

    for index, career_name in enumerate(
        career["careers"]
    ):

        with columns[index % 3]:
            st.info(career_name)

    # ========================================================
    # SCORE CHART
    # ========================================================

    st.subheader("📊 Your Career Areas")

    st.bar_chart(scores)

    # ========================================================
    # SUBJECTS
    # ========================================================

    st.subheader("📚 Subjects to Focus On")

    st.write(
        " • ".join(career["subjects"])
    )

    # ========================================================
    # SUBJECT RESULTS
    # ========================================================

    if subject_results:

        st.subheader("📝 Subject Knowledge Results")

        correct_count = sum(
            1
            for item in subject_results
            if item["is_correct"]
        )

        st.write(
            f"You answered {correct_count} out of "
            f"{len(subject_results)} selected-subject "
            f"questions correctly."
        )

        for item in subject_results:

            if item["is_correct"]:

                st.success(
                    f"✅ {item['subject']}: Correct"
                )

            else:

                st.warning(
                    f"📘 {item['subject']}: Review this topic "
                    f"and keep practising."
                )

    # ========================================================
    # WHAT TO DO
    # ========================================================

    st.subheader("✅ What You Should Do")

    for item in career["do"]:
        st.write(f"✅ {item}")

    # ========================================================
    # WHAT NOT TO DO
    # ========================================================

    st.subheader("🚫 What You Should NOT Do")

    for item in career["dont"]:
        st.write(f"❌ {item}")

    # ========================================================
    # INDIAN UNIVERSITIES
    # ========================================================

    st.header("🇮🇳 Indian Universities")

    st.info(
        "Tuition fees change by programme, category and academic "
        "year. Always verify the latest fee structure on the "
        "university's official website."
    )

    for university in career["universities"]:

        st.write(
            f"🎓 **{university}**"
        )

        st.caption(
            "Tuition: Check the latest official fee structure."
        )

    # ========================================================
    # STUDY ABROAD
    # ========================================================

    st.header("🌎 Study Abroad")

    st.write(
        "These universities are options students can explore "
        "for the selected career area. Admission requirements, "
        "tuition and scholarships vary."
    )

    for university in career["abroad"]:

        st.write(
            f"🌍 **{university}**"
        )

    # ========================================================
    # ABROAD CHECKLIST
    # ========================================================

    st.subheader("🗺️ Study-Abroad Checklist")

    checklist = [
        "Research the course.",
        "Check academic eligibility.",
        "Check tuition fees.",
        "Calculate living expenses.",
        "Look for scholarships.",
        "Check language requirements.",
        "Check entrance examinations.",
        "Check application deadlines.",
        "Research visa requirements.",
        "Check whether the qualification is suitable for your intended career."
    ]

    for item in checklist:
        st.write(f"☑️ {item}")

    # ========================================================
    # INDIA VS ABROAD
    # ========================================================

    st.subheader("🇮🇳 India vs 🌎 Abroad")

    comparison = {
        "Factor": [
            "Tuition",
            "Living Costs",
            "Travel",
            "Scholarships",
            "Admission",
            "International Exposure"
        ],
        "India": [
            "Often lower at public institutions",
            "Often lower",
            "Usually lower",
            "Government and university options",
            "Depends on programme",
            "Strong local exposure"
        ],
        "Abroad": [
            "Can be much higher",
            "Can be high",
            "International travel required",
            "University and government options",
            "Country-specific requirements",
            "Greater international exposure"
        ]
    }

    st.table(comparison)

    # ========================================================
    # SARVAM AI
    # ========================================================

    st.header("🤖 Sarvam AI Personalized Analysis")

    prompt = f"""
You are a helpful career exploration assistant for a school student.

Student name:
{student_name.strip()}

Top career area:
{top_career}

Top score:
{top_score}

Second career area:
{second_career}

Career scores:
{scores}

Subjects selected:
{q2}

Activities:
{q1}

Preferred work:
{q3}

Problem solving:
{q4}

Preferred skill:
{q5}

Preferred workplace:
{q6}

Teamwork:
{q7}

Motivation:
{q8}

Subject knowledge results:
{subject_results}

Provide a clear and encouraging career analysis.

Use these sections:

1. What this result means
2. Possible strengths
3. Careers to explore
4. Subjects to focus on
5. Skills to develop
6. What to do next
7. What to avoid
8. Indian study options
9. Study-abroad considerations
10. A simple 3-step roadmap

Do not say the quiz predicts the student's future.
Do not guarantee that a career is correct.
Explain that the result is a starting point for exploration.
Keep the advice suitable for a school student.
"""

    if st.button("✨ Generate My AI Career Analysis"):

        with st.spinner(
            "Sarvam AI is analysing your answers..."
        ):

            ai_result = get_sarvam_response(prompt)

        if ai_result.startswith(
            "Sarvam AI could not"
        ):

            st.error(ai_result)

        elif ai_result == (
            "Sarvam AI package is not installed."
        ):

            st.error(
                "Sarvam AI is not installed. "
                "Run: pip install -U sarvamai"
            )

        else:

            st.markdown(ai_result)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🧭 MapMyFuture")

    st.write(
        "Your career exploration assistant."
    )

    st.divider()

    st.write("### Assessment")

    st.write("👤 Student Name")
    st.write("🧠 25 Main Questions")
    st.write("✏️ 3 Fill-in-the-Blanks")
    st.write("📚 Subject Knowledge Check")
    st.write("🔒 Focus Mode")
    st.write("🎯 Career Matching")

    st.divider()

    st.write("### Career Map")

    st.write("🗺️ Subject Path")
    st.write("🧠 Skills Path")
    st.write("💼 Career Options")
    st.write("🚀 Preparation Path")
    st.write("🏆 Future Roadmap")

    st.divider()

    st.write("### Results")

    st.write("📊 Career Score")
    st.write("💼 Career Suggestions")
    st.write("📚 Subject Recommendations")
    st.write("🇮🇳 Indian Universities")
    st.write("🌎 Study Abroad")
    st.write("💰 Tuition Guidance")
    st.write("🤖 Sarvam AI Analysis")

    st.divider()

    st.caption(
        "MapMyFuture is a career exploration tool. "
        "The result is not a prediction of your future."
    )