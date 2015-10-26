donors = [
    ['John Lennon', 100.00, 50.00, 586.78],
    ['Paul McCartney', 200.00, 150.00],
    ['Ringo Starr', 1.00],
    ['George Harrison', 1000.00, 500.00, 1586.78],
    ['Yoko Ono', 275.50, 5.00]
]


def select_command():
    command = input("""Commands:
Enter 'Thank you' to send a thank you message.
Enter 'Report' to create a report.
Enter 'Home' to return to this screen.
Enter 'Quit' to exit My Donation Manager.""")
    print(command)
    return command


def write_email():
    full_name = input("Enter the donor's full name or type 'list' to see all donors.")

    while full_name == 'list':
        for donor in donors:
            print(donor[0])
        full_name = input("Enter the donor's full name or type 'list' to see all donors.")
        break

    if full_name not in donors:
        donors.append([full_name])

    donation_amount = input('Enter the donation amount.')

    while donation_amount:
        try:
            donation_amount = float(donation_amount)
            break
        except:
            donation_amount = input('Please enter a numeric value.')

    for donor in donors:
        if full_name == donor[0]:
            donor.append(donation_amount)

    thank_you = """Dear {},
    Thank you for your generous donation of ${}. You're
    the best!

    Sincerely,
    Your favorite charity """.format(full_name, donation_amount)

    print(thank_you)


def create_report():
    print('Donor\t\t\tTotal\t\tNumber\t\tAverage')
    for donor in donors:
        total_donation = sum(donor[1:])
        number_of_donations = len(donor[1:])
        average_donation = total_donation/number_of_donations
        print('{}\t\t{:.2f}\t\t{:d}\t\t{:.2f}'.format(donor[0], total_donation, number_of_donations, average_donation))

if __name__ == '__main__':
    command = select_command()
    

