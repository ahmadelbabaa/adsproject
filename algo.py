import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk

class Student:
    def __init__(self, student_name, graduation_year, degree):
        self.student_name = student_name
        self.graduation_year = graduation_year
        self.degree = degree

class Company:
    def __init__(self, company_name, field, position):
        self.company_name = company_name
        self.field = field
        self.position = position

# Creating instances of students and companies
students = [
    Student("Alice", 2024, "BDBA"),
    Student("Bob", 2023, "BDBA"),
    Student("Charlie", 2022, "BBA"),
    Student("David", 2021, "BCSAI"),
    Student("Eve", 2020, "BDBA")
]

companies = [
    Company("KPMG", "Data Science", "Data Science Intern"),
    Company("PWC", "Finance", "Finance Intern"),
    Company("Samsung", "Data Science", "Junior Data Analyst"),
    Company("Microsoft", "Technology and AI", "Software Engineer"),
    Company("Amazon", "Machine Learning and AI", "Machine Learning Engineer Junior")
]

# Create nodes for students and companies
nodes = [
    (student.student_name, {'type': 'student'}) for student in students
] + [
    (company.company_name, {'type': 'company'}) for company in companies
]

# Create a fully connected graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(nodes)

# Connect all students to all companies
edges = [(student.student_name, company.company_name) for student in students for company in companies]

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(12, 8))

pos = nx.spring_layout(G)
student_nodes = [node for node in G.nodes if G.nodes[node]['type'] == 'student']
company_nodes = [node for node in G.nodes if G.nodes[node]['type'] == 'company']

nx.draw_networkx_nodes(G, pos, nodelist=student_nodes, node_color='skyblue', node_size=500, label='Students')
nx.draw_networkx_nodes(G, pos, nodelist=company_nodes, node_color='lightgreen', node_size=500, label='Companies')
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos)

plt.title('Fully Connected Students and Companies Network')
plt.legend()
plt.axis('off')
plt.show()

# Employer View
class EmployerView:
    def __init__(self):
        self.app_employer = tk.Tk()
        self.app_employer.title("Employer View")

        tk.Label(self.app_employer, text="Enter Desired Student Degree:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.app_employer, text="Enter Interests of Students:").grid(row=1, column=0, padx=10, pady=10)

        self.degree_var = tk.StringVar()
        self.interests_var = tk.StringVar()

        degree_entry = tk.Entry(self.app_employer, textvariable=self.degree_var)
        degree_entry.grid(row=0, column=1, padx=10, pady=10)

        field_entry = tk.Entry(self.app_employer, textvariable=self.interests_var)
        field_entry.grid(row=1, column=1, padx=10, pady=10)

        find_button = tk.Button(self.app_employer, text="Find Students", command=self.find_internship)
        find_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.result_text = tk.StringVar()
        result_label = tk.Label(self.app_employer, textvariable=self.result_text, justify=tk.LEFT)
        result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def find_internship(self):
        selected_degree = self.degree_var.get()
        selected_interests = self.interests_var.get()

        matched_companies = self.match_company_with_student(selected_degree, selected_interests)

        self.result_text.set(
            f"Internship matches for {selected_degree} students in {selected_interests}:\n{', '.join(matched_companies)}")

    def match_company_with_student(self, selected_degree, selected_interests):
        matched_students = []
        for student in students:
            if student.degree == selected_degree and any(topic in student.degree for topic in selected_interests):
                matched_students.append(student.student_name)
        return matched_students

    def run(self):
        self.app_employer.mainloop()

# Student View
class StudentView:
    def __init__(self):
        self.app_student = tk.Tk()
        self.app_student.title("Student View")

        tk.Label(self.app_student, text="Enter Desired Field:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.app_student, text="Enter Preferred Position:").grid(row=1, column=0, padx=10, pady=10)

        self.field_var = tk.StringVar()
        self.position_var = tk.StringVar()

        degree_entry = tk.Entry(self.app_student, textvariable=self.field_var)
        degree_entry.grid(row=0, column=1, padx=10, pady=10)

        field_entry = tk.Entry(self.app_student, textvariable=self.position_var)
        field_entry.grid(row=1, column=1, padx=10, pady=10)

        find_button = tk.Button(self.app_student, text="Find Internship", command=self.find_internship_student)
        find_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.result_text_student = tk.StringVar()
        result_label = tk.Label(self.app_student, textvariable=self.result_text_student, justify=tk.LEFT)
        result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def find_internship_student(self):
        selected_field = self.field_var.get()
        selected_position = self.position_var.get()

        matched_students = self.match_students_with_company(selected_field, selected_position)

        self.result_text_student.set(
            f"Internship matches for {selected_field} companies with {selected_position}:\n{', '.join(matched_students)}")

    def match_students_with_company(self, selected_field, selected_position):
        matched_students = []
        for company in companies:
            if company.field == selected_field and any(topic in company.field for topic in selected_position):
                matched_students.append(company.company_name)
        return matched_students

    def run(self):
        self.app_student.mainloop()

# Run the GUIs
employer_view = EmployerView()
employer_view.run()

student_view = StudentView()
student_view.run()
