Departments = [
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Pediatrics",
    "Dermatology",
    "Psychiatry",
    "Radiology",
    "Gastroenterology",
    "Endocrinology",
    "Pulmonology",
    "Urology",
    "Ophthalmology",
    "Rheumatology",
    "Hematology",
    "Nephrology"
]
available_departments = [
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Pediatrics",
    "Dermatology",
    "Psychiatry",
    "Radiology",
    "Gastroenterology",
    "Endocrinology",
    "Pulmonology"
]
not_available_departments = [
    "Urology",
    "Ophthalmology",
    "Rheumatology",
    "Hematology",
    "Nephrology"
]
available_doctor_names = [
    "Dr. Smith",
    "Dr. Johnson",
    "Dr. Williams",
    "Dr. Brown",
    "Dr. Jones",
    "Dr. Miller",
    "Dr. Davis",
    "Dr. Garcia",
    "Dr. Rodriguez",
    "Dr. Wilson"
]
not_available_doctor_names = [
    "Dr. Martinez",
    "Dr. Anderson",
    "Dr. Taylor",
    "Dr. Thomas",
    "Dr. Hernandez"
]
emergency_departments = [
    "Cardiology",
    "Neurology",
    "Pulmonology"
]


def check_department_availability(Requested_Department):
    ad = []
    ud = []
    for i in Requested_Department:
        if i in available_departments:
            ad.append(i)
        else:
            ud.append(i)
    return ad, ud


def check_doctor_availability(requested_doctor_name):
    ad = []
    ud = []
    for i in requested_doctor_name:
        if i in available_doctor_names:
            ad.append(i)
        else:
            ud.append(i)
    return ad, ud


def get_department_names(department_numbers):
    requested_departments = []
    for i in department_numbers:
        if 1 <= i <= len(Departments):
            requested_departments.append(Departments[i - 1])
    return requested_departments

def get_doctor_names(doctor_numbers):
    doctor_names = sorted(
        available_doctor_names + not_available_doctor_names
    )
    requested_doctors = []
    for i in doctor_numbers:
        if 1 <= i <= len(doctor_names):
            requested_doctors.append(doctor_names[i - 1])
    return requested_doctors


def get_inputs():
    Patient_Name = input("Enter patient name: ")
    print("\nAvailable Departments:")
    for i, name in enumerate(Departments, start=1):
        print("{}. {}".format(i, name))
    Requested_Department = list(
        map(
            int,
            input("Enter requested department numbers (1-15): ").split(",")
        )
    )
    Requested_Department = get_department_names(Requested_Department)
    avalibility_Department, unavailable_Department = \
        check_department_availability(Requested_Department)
    print("\nRequested Departments:")
    print(Requested_Department)
    print("\nEnter previously visited departments:")
    previously_visited_departments = list(
        map(
            int,
            input("Enter department numbers (1-15): ").split(",")
        )
    )
    previously_visited_departments = get_department_names(
        previously_visited_departments
    )
    print("\nAvailable and Unavailable Doctors:")
    doctor_list = sorted(
        available_doctor_names + not_available_doctor_names
    )
    for i, name in enumerate(doctor_list, start=1):
        print("{}. {}".format(i, name))
    requested_doctor_name = list(
        map(
            int,
            input("Enter requested doctor numbers (1-15): ").split(",")
        )
    )
    requested_doctor_name = get_doctor_names(requested_doctor_name)
    available_doctor, unavailable_doctor = \
        check_doctor_availability(requested_doctor_name)
    emergency_department = input(
        "Is it an emergency department? (yes/no): "
    ).lower()
    return (
        Patient_Name,
        Requested_Department,
        avalibility_Department,
        unavailable_Department,
        previously_visited_departments,
        requested_doctor_name,
        available_doctor,
        unavailable_doctor,
        emergency_department
    )


if __name__ == "__main__":

    (
        Patient_Name,
        Requested_Department,
        avalibility_Department,
        unavailable_Department,
        previously_visited_departments,
        requested_doctor_name,
        available_doctor,
        unavailable_doctor,
        emergency_department
    ) = get_inputs()

    requested_set = set(Requested_Department)
    available_set = set(available_departments)
    previous_set = set(previously_visited_departments)
    emergency_set = set(emergency_departments)
    common_departments = requested_set & available_set
    unavailable_set = requested_set - available_set
    previous_departments = requested_set & previous_set
    emergency_departments_requested = requested_set & emergency_set
    all_departments = available_set | set(not_available_departments)
    duplicate_requests = []
    for department in Requested_Department:
        if Requested_Department.count(department) > 1:
            if department not in duplicate_requests:
                duplicate_requests.append(department)
    if emergency_departments_requested:
        recommended_department = list(
            emergency_departments_requested
        )[0]
    elif common_departments:
        recommended_department = list(
            common_departments
        )[0]
    else:
        recommended_department = "No Department Available"
    if emergency_departments_requested:
        final_status = "Emergency Appointment"
    elif common_departments and available_doctor:
        final_status = "Appointment Confirmed"
    elif common_departments:
        final_status = "Doctor Unavailable"
    else:
        final_status = "Appointment Not Available"
    print("\n")
    print("=" * 50)
    print("          PATIENT APPOINTMENT REPORT")
    print("=" * 50)
    print("\nPatient Name:")
    print(Patient_Name)
    print("\nRequested Departments:")
    for i, department in enumerate(Requested_Department, start=1):
        print("{}. {}".format(i, department))
    print("\nAvailable Departments:")
    for department in avalibility_Department:
        print("-", department)
    print("\nUnavailable Departments:")
    for department in unavailable_Department:
        print("-", department)
    print("\nCommon Departments:")
    for department in common_departments:
        print("-", department)
    print("\nDuplicate Requests:")
    if duplicate_requests:
        for department in duplicate_requests:
            print("-", department)
    else:
        print("None")
    print("\nPreviously Visited Departments:")
    if previous_departments:
        for department in previous_departments:
            print("-", department)
    else:
        print("None")
    print("\nEmergency Departments:")
    if emergency_departments_requested:
        for department in emergency_departments_requested:
            print("-", department)
    else:
        print("None")
    print("\nRequested Doctors:")
    for doctor in requested_doctor_name:
        print("-", doctor)
    print("\nAvailable Doctors:")
    if available_doctor:
        for doctor in available_doctor:
            print("-", doctor)
    else:
        print("None")
    print("\nUnavailable Doctors:")
    if unavailable_doctor:
        for doctor in unavailable_doctor:
            print("-", doctor)
    else:
        print("None")
    print("\nRecommended Department:")
    print(recommended_department)
    print("\nFinal Appointment Status:")
    print(final_status)
    print("\nAll Hospital Departments:")
    print(all_departments)
    print("\nIs Recommended Department an Emergency Department?")
    if recommended_department in emergency_set:
        print("Yes")
    else:
        print("No")
    print("\n")
    print("=" * 50)