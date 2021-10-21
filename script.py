class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  def estimated_insurance_cost(self):
    try:
      estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500 
      print('{name}\'s estimated insurance costs is {estimated} dollars.'.format(name = self.name, estimated = estimated_cost))
    except:
      print('Please check that every imput but name are numbers')
  def update_age(self, new_age):
    self.age = new_age
    print('{name} is now {age} years old.'.format(name = self.name, age = self.age))   
    patient1.estimated_insurance_cost()

  def update_number_of_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print('{name} has {children} child.'.format(name = self.name, children = self.num_of_children))
    else:
      print('{name} has {children} children.'.format(name = self.name, children = self.num_of_children))
    patient1.estimated_insurance_cost()

  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print("{name}'s new updated BMI is: {bmi}.".format(self.name, self.bmi) )
    self.estimated_insurance_cost()

  def update_smoker(self, new_smoker):
    self.smoker = new_smoker
    if new_smoker == 1:
      print("{name} became a smoker.".format(name = self.name))
    else:
      print("Congrats! {name} quit smoking".format(name = self.name))
    self.estimated_insurance_cost()

  def patient_profile(self):
    patient_information = {}
    patient_information['Name'] = self.name
    patient_information['Age'] = self.age
    patient_information['Sex'] = self.sex
    patient_information['BMI'] = self.bmi
    patient_information['Number of Children'] = self.num_of_children
    patient_information['Smoker'] = self.smoker
    return patient_information

    # add more parameters here
patient1 = Patient('John Doe', 25, 1, 22.2, 0, 0)
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_number_of_children(1)
print(patient1.patient_profile())
patient1.update_smoker(1)