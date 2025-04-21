import streamlit as st
from datetime import datetime, date

# Set page config for a wider layout and custom title
st.set_page_config(
    page_title="Study Buddy 📚",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a more modern look
st.markdown("""
    <style>
    .stButton button {
        background-color: #FF6B6B;
        color: white;
        border-radius: 20px;
        padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-color: #FF8787;
    }
    .stTextInput input {
        border-radius: 15px;
    }
    .stSelectbox select {
        border-radius: 15px;
    }
    .task-done {
        text-decoration: line-through;
        color: #888888;
    }
    </style>
    """, unsafe_allow_html=True)

## Dishan 
def load_todos():
    if 'todos' not in st.session_state:
        st.session_state.todos = []
    return st.session_state.todos

def save_todos(todos):
    st.session_state.todos = todos

def todo_list():
    st.header("✅ Todo List")
    st.write("Stay organized and crush your goals! 🎯")
    
    # Load existing todos
    todos = load_todos()
    
    # Add new todo section
    st.markdown("### Add New Task ✨")
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        new_todo = st.text_input("What do you need to do? 📝", key="new_todo")
    
    with col2:
        category = st.selectbox(
            "Category 📑",
            ["📚 Study", "📝 Assignment", "📖 Reading", "🎯 Project", "🎨 Other"],
            key="category"
        )
    
    with col3:
        priority = st.selectbox(
            "Priority ⚡",
            ["🔥 High", "⚡ Medium", "💫 Low"],
            key="priority"
        )
    
    col4, col5 = st.columns(2)
    
    with col4:
        due_date = st.date_input("Due Date 📅", min_value=date.today())
    
    with col5:
        if st.button("Add Task ➕", key="add_task"):
            if new_todo:
                todos.append({
                    "task": new_todo,
                    "category": category,
                    "priority": priority,
                    "due_date": due_date.strftime("%Y-%m-%d"),
                    "completed": False,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                save_todos(todos)
                st.rerun()

    # Filter and sort options
    st.markdown("### Your Tasks 📋")
    col6, col7 = st.columns(2)
    
    with col6:
        filter_category = st.multiselect(
            "Filter by Category 🔍",
            ["📚 Study", "📝 Assignment", "📖 Reading", "🎯 Project", "🎨 Other"],
            default=[]
        )
    
    with col7:
        sort_by = st.selectbox(
            "Sort by 📊",
            ["Due Date ⏰", "Priority ⚡", "Category 📑"],
        )

    # Display todos
    if todos:
        # Filter todos
        filtered_todos = todos
        if filter_category:
            filtered_todos = [todo for todo in todos if todo["category"] in filter_category]
        
        # Sort todos
        if sort_by == "Due Date ⏰":
            filtered_todos.sort(key=lambda x: x["due_date"])
        elif sort_by == "Priority ⚡":
            priority_order = {"🔥 High": 0, "⚡ Medium": 1, "💫 Low": 2}
            filtered_todos.sort(key=lambda x: priority_order[x["priority"]])
        else:
            filtered_todos.sort(key=lambda x: x["category"])

        # Display todos in a modern way
        for idx, todo in enumerate(filtered_todos):
            col8, col9, col10, col11 = st.columns([3, 2, 2, 1])
            
            with col8:
                done = st.checkbox(
                    todo["task"],
                    key=f"todo_{idx}",
                    value=todo["completed"]
                )
                if done != todo["completed"]:
                    todos[todos.index(todo)]["completed"] = done
                    save_todos(todos)
            
            with col9:
                st.write(f"{todo['category']} | {todo['priority']}")
            
            with col10:
                st.write(f"Due: {todo['due_date']}")
            
            with col11:
                if st.button("🗑️", key=f"delete_{idx}"):
                    todos.remove(todo)
                    save_todos(todos)
                    st.rerun()
        
        # Task statistics
        st.markdown("### Quick Stats 📊")
        col12, col13, col14 = st.columns(3)
        
        completed_tasks = len([todo for todo in todos if todo["completed"]])
        total_tasks = len(todos)
        
        with col12:
            st.metric("Total Tasks 📝", total_tasks)
        
        with col13:
            st.metric("Completed ✅", completed_tasks)
        
        with col14:
            completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
            st.metric("Completion Rate 🎯", f"{completion_rate:.1f}%")
    
    else:
        st.info("No tasks yet! Add some tasks to get started! ✨")

## Siddharth 
def grade_calculator():
    st.header("📊 Grade Calculator")
    st.write("Let's see how you're doing! 🤓")
    
    col1, col2 = st.columns(2)
    with col1:
        total_marks = st.number_input("Total Marks 📝", min_value=1, value=100)
    with col2:
        obtained_marks = st.number_input("Marks You Got ✍️", min_value=0, max_value=total_marks, value=0)
    
    if st.button("Calculate My Grade 🎯"):
        percentage = (obtained_marks / total_marks) * 100
        grade = calculate_grade(percentage)
        
        # Emoji based on grade
        grade_emoji = {
            'A': '🌟', 'B': '✨', 'C': '👍', 'D': '😊', 'F': '💪'
        }
        
        st.markdown(f"""
        ### Results 📊
        - Percentage: **{percentage:.2f}%**
        - Grade: **{grade}** {grade_emoji[grade]}
        """)

def calculate_grade(percentage):
    if percentage >= 90: return 'A'
    elif percentage >= 80: return 'B'
    elif percentage >= 70: return 'C'
    elif percentage >= 60: return 'D'
    else: return 'F'

## Jay
def sgpa_calculator():
    st.header("🎓 SGPA Calculator")
    st.write("Let's calculate your semester GPA! 📚")
    
    num_subjects = st.number_input("Number of Subjects 📚", min_value=1, max_value=10, value=5)
    
    total_credits = 0
    weighted_grade_points = 0
    
    st.markdown("### Enter Your Grades 📝")
    for i in range(int(num_subjects)):
        col1, col2 = st.columns(2)
        with col1:
            grade_points = st.number_input(f"Grade Points for Subject {i+1} 📊", min_value=0.0, max_value=10.0, value=0.0)
        with col2:
            credits = st.number_input(f"Credits for Subject {i+1} 💫", min_value=1, max_value=6, value=3)
        weighted_grade_points += grade_points * credits
        total_credits += credits
    
    if st.button("Calculate SGPA 🎯"):
        if total_credits > 0:
            sgpa = weighted_grade_points / total_credits
            st.markdown(f"""
            ### Your Results ✨
            SGPA: **{sgpa:.2f}** 🎉
            """)
        else:
            st.error("Total credits cannot be zero! 😅")

## Priyansh
def physics_solver():
    st.header("⚡ Physics Formula Solver")
    st.write("Let's solve some physics problems! 🔬")
    
    formulas = {
        "Force (F = m × a)": ["mass (kg)", "acceleration (m/s²)", "Force in (N)"],
        "Energy (E = m × c²)": ["mass (kg)", None, "Energy in (J)"],
        "Work Done (W = F × d)": ["force (N)", "distance (m)", "Work Done in (J)"],
        "Power (P = W ÷ t)": ["work done (J)", "time (s)", "Power in (W)"],
        "Kinetic Energy (KE = ½ × m × v²)": ["mass (kg)", "velocity (m/s)", "Kinetic Energy in (J)"],
        "Potential Energy (PE = m × g × h)": ["mass (kg)", "height (m)", "Potential Energy in (J)"],
        "Momentum (p = m × v)": ["mass (kg)", "velocity (m/s)", "Momentum in (kg·m/s)"],
        "Density (ρ = m ÷ V)": ["mass (kg)", "volume (m³)", "Density in (kg/m³)"],
        "Pressure (P = F ÷ A)": ["force (N)", "area (m²)", "Pressure in (Pa)"],
        "Ohm’s Law (V = I × R)": ["current (A)", "resistance (Ω)", "Voltage in (V)"],
        "Wave Speed (v = f × λ)": ["frequency (Hz)", "wavelength (m)", "Wave Speed in (m/s)"]
    }
    
    selected_formula = st.selectbox("Choose your formula 📐", list(formulas.keys()))
    
    col1, col2 = st.columns(2)
    inputs = {}
    
    with col1:
        if formulas[selected_formula][0]:
            inputs['first'] = st.number_input(f"Enter {formulas[selected_formula][0]} 📏", value=0.0)
    with col2:
        if formulas[selected_formula][1]:
            inputs['second'] = st.number_input(f"Enter {formulas[selected_formula][1]} 📏", value=0.0)
    
    if st.button("Solve It! 🎯"):
        result = 0
        if selected_formula.startswith("Force"):
            result = inputs['first'] * inputs['second']
        elif selected_formula.startswith("Energy"):
            c = 3e8
            result = inputs['first'] * (c ** 2)
        elif selected_formula.startswith("Work"):
            result = inputs['first'] * inputs['second']
        elif selected_formula.startswith("Power"):
            result = inputs['first'] / inputs['second'] if inputs['second'] != 0 else 0
        elif selected_formula.startswith("Kinetic"):
            result = 0.5 * inputs['first'] * (inputs['second'] ** 2)
        elif selected_formula.startswith("Potential"):
            g = 9.81  # Gravity (m/s²)
            result = inputs['first'] * g * inputs['second']
        elif selected_formula.startswith("Momentum"):
            result = inputs['first'] * inputs['second']
        elif selected_formula.startswith("Density"):
            result = inputs['first'] / inputs['second'] if inputs['second'] != 0 else 0
        elif selected_formula.startswith("Pressure"):
            result = inputs['first'] / inputs['second'] if inputs['second'] != 0 else 0
        elif selected_formula.startswith("Ohm"):
            result = inputs['first'] * inputs['second']
        elif selected_formula.startswith("Wave"):
            result = inputs['first'] * inputs['second']    
        
        st.markdown(f"""
        ### Result ✨
        {formulas[selected_formula][2]}: **{result:.4f}**
        """)

## Sidra
def unit_converter():
    st.header("📏 Unit Converter")
    st.write("Convert between different units easily! 🔄")
    
    conversion_types = {
        "Length 📏": {
            "Meters to Feet": lambda x: x * 3.281,
            "Feet to Meters": lambda x: x / 3.281,
            "Kilometers to Miles": lambda x: x * 0.621,
            "Miles to Kilometers": lambda x: x / 0.621,
            "Centimeters to Inches": lambda x: x / 2.54,
            "Inches to Centimeters": lambda x: x * 2.54
        },
        "Weight ⚖️": {
            "Kilograms to Pounds": lambda x: x * 2.205,
            "Pounds to Kilograms": lambda x: x / 2.205,
            "Grams to Ounces": lambda x: x / 28.35,
            "Ounces to Grams": lambda x: x * 28.35

        },
        "Temperature 🌡️": {
            "Celsius to Fahrenheit": lambda x: (x * 9/5) + 32,
            "Fahrenheit to Celsius": lambda x: (x - 32) * 5/9
        },
        "Volume 🫙": {
            "Liters to Gallons": lambda x: x * 0.264,
            "Gallons to Liters": lambda x: x / 0.264
        },
        "Time ⏳": {
            "Hours to Minutes": lambda x: x * 60,
            "Minutes to Hours": lambda x: x / 60,
            "Minutes to Seconds": lambda x: x * 60,
            "Seconds to Minutes": lambda x: x / 60
        },
        "Area 🏡": {
            "Square Meters to Square Feet": lambda x: x * 10.764,
            "Square Feet to Square Meters": lambda x: x / 10.764,
            "Acres to Hectares": lambda x: x * 0.4047,
            "Hectares to Acres": lambda x: x / 0.4047
        },
        "Pressure 🔄": {
            "Pascals to Atmospheres": lambda x: x / 101325,
            "Atmospheres to Pascals": lambda x: x * 101325,
            "Bar to PSI": lambda x: x * 14.5038,
            "PSI to Bar": lambda x: x / 14.5038
        },
    } 
    
    # Select conversion category
    category = st.selectbox("Select Category 📊", list(conversion_types.keys()))
    
    # Select specific conversion
    conversion = st.selectbox("Select Conversion 🔄", list(conversion_types[category].keys()))
    
    # Input value
    col1, _ = st.columns(2)
    with col1:
        value = st.number_input("Enter Value 📝", value=0.0)
    
    # Calculate and display result
    if st.button("Convert! 🎯"):
        result = conversion_types[category][conversion](value)
        
        # Format units for display
        from_unit, to_unit = conversion.split(" to ")
        
        st.markdown(f"""
        ### Result ✨
        **{value} {from_unit}** = **{result:.2f} {to_unit}** 🎉
        """)

def main():
    st.sidebar.title("Study Buddy 📚")
    st.sidebar.markdown("Your personal academic assistant! ✨")
    
    # Get current time to personalize greeting
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
    elif current_hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
        
    st.sidebar.markdown(f"### {greeting} Bestie! 👋")
    
    options = {
        "🏠 Home": None,
        "✅ Todo List": todo_list,
        "📊 Grade Calculator": grade_calculator,
        "🎓 SGPA Calculator": sgpa_calculator,
        "⚡ Physics Solver": physics_solver,
        "📏 Unit Converter": unit_converter
    }
    
    choice = st.sidebar.radio("Let's get productive! 🚀", options.keys())
    
    if choice == "🏠 Home":
        st.markdown("""
        # Welcome to Study Buddy! 🌟
        
        Your all-in-one study companion that makes learning fun! ✨
        
        ### What can I help you with? 📚
        
        - ✅ **Todo List**: Keep track of your tasks and deadlines
        - 📊 **Grade Calculator**: Calculate your grades and see where you stand
        - 🎓 **SGPA Calculator**: Keep track of your academic performance
        - ⚡ **Physics Solver**: Solve physics problems
        - 📏 **Unit Converter**: Convert between different units easily            
        
        Choose an option from the sidebar to get started! 🚀
        """)
    else:
        options[choice]()

if __name__ == "__main__":
    main()