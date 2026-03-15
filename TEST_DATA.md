# 🧪 Test Data - Sample Resumes & Job Descriptions

Use these to test different role matches and verify the system gives correct suggestions.

---

## 1️⃣ BACKEND ENGINEER TEST

### Backend Resume
```
John Smith
Email: john@example.com
Phone: (555) 123-4567

PROFESSIONAL SUMMARY
Senior Backend Engineer with 6 years building scalable APIs and microservices.

EXPERIENCE
Senior Backend Engineer - TechCorp (2020-2024)
- Designed and implemented RESTful APIs using Python and FastAPI
- Built microservices architecture handling 1M+ requests/day
- Optimized PostgreSQL queries, improved performance by 60%
- Deployed applications using Docker and Kubernetes on AWS
- Led team of 3 engineers in agile environment

Software Engineer - WebDev Inc (2018-2020)
- Developed backend services with Python and Django
- Managed MySQL and PostgreSQL databases
- Implemented CI/CD pipelines with GitHub Actions

SKILLS
Python, FastAPI, Django, Node.js, REST API, GraphQL, PostgreSQL, MySQL, MongoDB, Docker, Kubernetes, AWS, Git, Linux, Agile, SQL

EDUCATION
Bachelor of Science in Computer Science
State University, 2018
```

### Backend Job Description
```
Senior Backend Engineer

ABOUT THE ROLE
We're seeking an experienced Backend Engineer to build and maintain our core APIs and microservices.

REQUIRED SKILLS
- 5+ years backend development experience
- Expert in Python, FastAPI or Django
- Strong SQL and database design (PostgreSQL, MySQL)
- REST API and GraphQL experience
- Docker and container orchestration
- AWS or cloud platform experience
- Git and version control
- Agile/Scrum methodology

NICE TO HAVE
- Kubernetes experience
- Microservices architecture knowledge
- Message queues (RabbitMQ, Kafka)
- System design experience
- Open source contributions
```

**Expected Result:** High match (80%+), suggestions for Kubernetes, message queues, system design

---

## 2️⃣ FRONTEND ENGINEER TEST

### Frontend Resume
```
Sarah Johnson
Email: sarah@example.com
Phone: (555) 987-6543

PROFESSIONAL SUMMARY
Frontend Engineer with 5 years building responsive, accessible web applications using React.

EXPERIENCE
Senior Frontend Developer - DesignCo (2021-2024)
- Built responsive web applications using React 18 and TypeScript
- Implemented pixel-perfect designs with CSS3, Tailwind CSS
- Improved Core Web Vitals, achieving 95+ Lighthouse score
- Led accessibility improvements (WCAG 2.1 AA compliance)
- Wrote unit tests with Jest and integration tests with Cypress
- Mentored 2 junior developers

Frontend Engineer - StartupXYZ (2019-2021)
- Developed components using React and Redux
- Implemented responsive designs for mobile and desktop
- Set up CI/CD pipelines with GitHub Actions

SKILLS
JavaScript, TypeScript, React, Next.js, HTML5, CSS3, Tailwind, Redux, Jest, Cypress, Webpack, Git, Accessibility, Responsive Design, Performance Optimization

EDUCATION
Bachelor of Science in Computer Science
Tech University, 2019
```

### Frontend Job Description
```
Senior Frontend Engineer

ABOUT THE ROLE
Join our team to build beautiful, performant user interfaces using modern web technologies.

REQUIRED SKILLS
- 5+ years frontend development
- Expert in JavaScript/TypeScript and React
- HTML5, CSS3, responsive design
- Component-based architecture
- Testing (Jest, React Testing Library, Cypress)
- Git and version control
- Performance optimization
- Accessibility (WCAG standards)

NICE TO HAVE
- Next.js experience
- State management (Redux, Zustand)
- Design tools (Figma)
- Browser DevTools knowledge
- PWA development
```

**Expected Result:** High match (85%+), suggestions for Next.js, design tools, PWA

---

## 3️⃣ MACHINE LEARNING ENGINEER TEST

### ML Resume
```
David Chen
Email: david@example.com
Phone: (555) 456-7890

PROFESSIONAL SUMMARY
ML Engineer with 4 years experience developing and deploying machine learning models.

EXPERIENCE
Machine Learning Engineer - DataAI Corp (2021-2024)
- Developed ML models using Python, TensorFlow, and PyTorch
- Preprocessed large datasets using Pandas and NumPy
- Built NLP models for text classification (92% accuracy)
- Implemented CNN for computer vision tasks (image recognition)
- Deployed models using Docker and AWS SageMaker
- Wrote SQL queries for data extraction from PostgreSQL

Data Science Intern - Research Lab (2020-2021)
- Analyzed datasets and built statistical models
- Created data visualizations using Python
- Learned deep learning and neural networks

SKILLS
Python, TensorFlow, PyTorch, Scikit-learn, Pandas, NumPy, SQL, Statistics, Linear Algebra, Probability, NLP, Computer Vision, Deep Learning, Jupyter, Git, AWS, Docker

EDUCATION
Bachelor of Science in Data Science
University of Technology, 2020
```

### ML Job Description
```
Junior Machine Learning Engineer

ABOUT THE ROLE
Support development, training, and deployment of ML models under guidance of senior engineers.

REQUIRED SKILLS
- Proficiency in Python and ML libraries (TensorFlow, PyTorch, Scikit-learn)
- Basic knowledge of statistics, linear algebra, and probability
- Familiarity with SQL, Pandas, NumPy, and Git
- Strong problem-solving skills

NICE TO HAVE
- NLP or Computer Vision experience
- Deep learning knowledge
- Jupyter Notebook experience
- AWS or cloud platform experience
- Docker experience
- Deployment experience
```

**Expected Result:** Very high match (90%+), suggestions for advanced ML specialization

---

## 4️⃣ FULLSTACK ENGINEER TEST

### Fullstack Resume
```
Emily Rodriguez
Email: emily@example.com
Phone: (555) 234-5678

PROFESSIONAL SUMMARY
Fullstack Engineer with 4 years building end-to-end web applications.

EXPERIENCE
Fullstack Engineer - AppBuilder (2021-2024)
- Built full-featured web applications with React and Node.js
- Designed RESTful APIs using Express.js
- Managed PostgreSQL databases and built schemas
- Implemented authentication and authorization
- Deployed applications on Heroku and AWS
- Wrote tests with Jest and React Testing Library

Junior Developer - WebStudio (2020-2021)
- Developed frontend components in React
- Built backend APIs with Python and Flask
- Collaborated with designers on UI/UX

SKILLS
JavaScript, TypeScript, React, Node.js, Express.js, Python, Flask, HTML5, CSS3, PostgreSQL, MongoDB, REST API, JWT, Git, Docker, AWS, Jest, Testing

EDUCATION
Bootcamp in Full Stack Web Development
CodingAcademy, 2020
```

### Fullstack Job Description
```
Fullstack Engineer

ABOUT THE ROLE
Build complete web solutions from database to user interface.

REQUIRED SKILLS
- JavaScript/TypeScript expertise
- React or Vue.js frontend skills
- Node.js or Python backend skills
- SQL and database design
- REST API development
- Git version control
- Testing (unit and integration)

NICE TO HAVE
- Docker containerization
- CI/CD pipeline experience
- Cloud deployment (AWS, Heroku)
- Authentication/security knowledge
- Agile methodology
```

**Expected Result:** High match (80%+), fullstack-specific suggestions

---

## 5️⃣ WRONG MATCH TEST (Backend Resume + Frontend Job)

### Use:
- **Resume:** Backend Engineer Resume (Section 1)
- **Job Description:** Frontend Job Description (Section 2)

**Expected Result:** LOW match (20-30%), suggestions to add:
- React, TypeScript
- CSS, HTML, responsive design
- Frontend testing (Jest, Cypress)
- Accessibility

---

## 6️⃣ HOW TO TEST

**Step 1:** Copy a resume from above
**Step 2:** Copy the matching job description
**Step 3:** Upload PDF or paste resume text
**Step 4:** Paste job description
**Step 5:** Click "Analyze Resume"

**Check Results:**
- ✅ ATS Score should be HIGH for matching roles
- ✅ Matched skills should show role-specific skills
- ✅ Missing skills should be few
- ✅ Suggestions should be relevant to the role

---

## 🎯 Test Cases to Verify

| Resume | Job | Expected Match | Purpose |
|--------|-----|---|---|
| Backend | Backend | 80%+ | Verify backend role detection |
| Frontend | Frontend | 85%+ | Verify frontend role detection |
| ML | ML | 90%+ | Verify ML role detection |
| Fullstack | Fullstack | 80%+ | Verify fullstack role detection |
| Backend | Frontend | 20-30% | Verify cross-role mismatch |
| Frontend | Backend | 25-35% | Verify opposite role mismatch |
| ML | Backend | 40-50% | Verify partial overlap |

---

## 📊 What To Look For

**Good Results:**
- ✅ Matched skills list contains role-specific technologies
- ✅ Missing skills are relevant to the job
- ✅ Suggestions are actionable (learn framework X, improve skill Y)
- ✅ ATS score reflects actual skill match

**Bad Results (Need to Fix):**
- ❌ Backend resume shows frontend suggestions
- ❌ Frontend resume shows ML suggestions
- ❌ Unrelated skills in matched list
- ❌ Score doesn't reflect actual match

---

**Use this data to test and verify the system works correctly!**
