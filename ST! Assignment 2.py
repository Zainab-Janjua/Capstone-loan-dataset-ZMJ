import tkinter as tk
import Model


class LoanGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("Loan Applicant Predictor")
        self.main_window.geometry("1000x650")

        # Create three frames to group widgets.
        self.top_frame_gender = tk.Frame()
        self.top2_frame_married = tk.Frame()
        self.top3_frame_dependants = tk.Frame()
        self.top4_frame_education = tk.Frame()
        self.mid_frame_self_employed = tk.Frame()
        self.mid2_frame_applicant_income = tk.Frame()
        self.mid3_frame_coapplicant_income = tk.Frame()
        self.mid4_frame_loan_amount = tk.Frame()
        self.lower_frame_term = tk.Frame()
        self.lower2_frame_credit_history = tk.Frame()
        self.lower3_frame_area = tk.Frame()
        self.button_frame = tk.Frame()
        self.bottombottom_frame = tk.Frame()

        # Create the widgets for the top frame and pack them( a label and atext box)
        self.top_frame_gender_label = tk.Label(self.top_frame_gender, text=" Gender: (male = 1  or female = 0)")
        self.top_frame_gender_entry = tk.Entry(self.top_frame_gender, bg='light grey', bd=2, width=10)
        self.top_frame_gender_label.pack(side='left')
        self.top_frame_gender_entry.pack(side='left')

        self.top2_frame_married_label = tk.Label(self.top2_frame_married, text=" Married: (yes = 1 or no = 0) ")
        self.top2_frame_married_entry = tk.Entry(self.top2_frame_married, bg='light grey', bd=2, width=10)
        self.top2_frame_married_label.pack(side='left')
        self.top2_frame_married_entry.pack(side='left')

        self.top3_frame_dependants_label = tk.Label(self.top3_frame_dependants, text=" Number of Dependants: ")
        self.top3_frame_dependants_entry = tk.Entry(self.top3_frame_dependants, bg='light grey', bd=2, width=10)
        self.top3_frame_dependants_label.pack(side='left')
        self.top3_frame_dependants_entry.pack(side='left')

        self.top4_frame_education_label = tk.Label(self.top4_frame_education,
                                                   text=" Education: (Graduate = 1 or Not Graduate = 0) ")
        self.top4_frame_education_entry = tk.Entry(self.top4_frame_education, bg='light grey', bd=2, width=10)
        self.top4_frame_education_label.pack(side='left')
        self.top4_frame_education_entry.pack(side='left')

        # Create the widgets for the middle frame and pack them( a label and a text box)
        self.mid_frame_self_employed_label = tk.Label(self.mid_frame_self_employed, text="Self Employed (yes = 1 or no = 0): ")
        self.mid_frame_self_employed_entry = tk.Entry(self.mid_frame_self_employed, bg='light grey', bd=2, width=10)
        self.mid_frame_self_employed_label.pack(side='left')
        self.mid_frame_self_employed_entry.pack(side='left')

        self.mid2_frame_applicant_income_label = tk.Label(self.mid2_frame_applicant_income, text=" Applicant Income: ")
        self.mid2_frame_applicant_income_entry = tk.Entry(self.mid2_frame_applicant_income, bg='light grey', bd=2,
                                                          width=10)
        self.mid2_frame_applicant_income_label.pack(side='left')
        self.mid2_frame_applicant_income_entry.pack(side='left')

        self.mid3_frame_coapplicant_income_label = tk.Label(self.mid3_frame_coapplicant_income,
                                                            text=" Coapplicant Income: ")
        self.mid3_frame_coapplicant_income_entry = tk.Entry(self.mid3_frame_coapplicant_income, bg='light grey', bd=2,
                                                            width=10)
        self.mid3_frame_coapplicant_income_label.pack(side='left')
        self.mid3_frame_coapplicant_income_entry.pack(side='left')

        self.mid4_frame_loan_amount_label = tk.Label(self.mid4_frame_loan_amount, text=" Loan Amount: ")
        self.mid4_frame_loan_amount_entry = tk.Entry(self.mid4_frame_loan_amount, bg='light grey', bd=2, width=10)
        self.mid4_frame_loan_amount_label.pack(side='left')
        self.mid4_frame_loan_amount_entry.pack(side='left')

        # Create the widgets for the lower frame and pack them( a label and a text box)
        self.lower_frame_term_label = tk.Label(self.lower_frame_term, text="Term (between 1 and 360): ")
        self.lower_frame_term_entry = tk.Entry(self.lower_frame_term, bg='light grey', bd=2, width=10)
        self.lower_frame_term_label.pack(side='left')
        self.lower_frame_term_entry.pack(side='left')

        self.lower2_frame_credit_history_label = tk.Label(self.lower2_frame_credit_history, text=" Credit history (in numbers): ")
        self.lower2_frame_credit_history_entry = tk.Entry(self.lower2_frame_credit_history, bg='light grey', bd=2,
                                                          width=10)
        self.lower2_frame_credit_history_label.pack(side='left')
        self.lower2_frame_credit_history_entry.pack(side='left')

        self.lower3_frame_area_label = tk.Label(self.lower3_frame_area, text=" Area (Urban = 1, Rural = 2 or semiurban = 3): ")
        self.lower3_frame_area_entry = tk.Entry(self.lower3_frame_area, bg='light grey', bd=2, width=10)
        self.lower3_frame_area_label.pack(side='left')
        self.lower3_frame_area_entry.pack(side='left')

        # Create the widgets for the button frame and pack them( calc button and a quit button)
        calc_button = tk.Button(self.button_frame, text="Calculate eligiblity", command=self.calc_loan)
        quit_button = tk.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        calc_button.pack(side='left')
        quit_button.pack(side='left')

        # Pack all the frames.
        self.top_frame_gender.pack()
        self.top2_frame_married.pack()
        self.top3_frame_dependants.pack()
        self.top4_frame_education.pack()
        self.mid_frame_self_employed.pack()
        self.mid2_frame_applicant_income.pack()
        self.mid3_frame_coapplicant_income.pack()
        self.mid4_frame_loan_amount.pack()
        self.lower_frame_term.pack()
        self.lower2_frame_credit_history.pack()
        self.lower3_frame_area.pack()
        self.button_frame.pack()
        self.bottombottom_frame.pack()

        # Enter the tkinter main loop.
        tk.mainloop()

    def calc_loan(self):
        Gender = float(self.top_frame_gender_entry.get())
        Married = float(self.top2_frame_married_entry.get())
        Dependents = float(self.top3_frame_dependants_entry.get())
        Education = float(self.top4_frame_education_entry.get())
        Self_Employed = float(self.mid_frame_self_employed_entry.get())
        Applicant_Income = float(self.mid2_frame_applicant_income_entry.get())
        Coapplicant_Income = float(self.mid3_frame_coapplicant_income_entry.get())
        Loan_Amount = float(self.mid4_frame_loan_amount_entry.get())
        Term = float(self.lower_frame_term_entry.get())
        Credit_History = float(self.lower2_frame_credit_history_entry.get())
        Area = float(self.lower3_frame_area_entry.get())

        loan_info = (
        Gender, Married, Dependents, Education, Self_Employed, Applicant_Income, Coapplicant_Income, Loan_Amount, Term,
        Credit_History, Area)
        prediction = Model.best_model.predict([loan_info])

        if prediction == [0]:
            Not_eligible = tk.Label(self.bottombottom_frame, text="Sorry, You are not eligible for a loan.")
            Not_eligible.pack()

        else:
            is_eligible = tk.Label(self.bottombottom_frame, text=" You are eligible for a loan")
            is_eligible.pack()


myGUI = LoanGUI()
