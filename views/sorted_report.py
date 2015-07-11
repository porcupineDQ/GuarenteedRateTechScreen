__author__ = 'dqin2'

from reports.directory import Directory

if __name__ == '__main__':
    report = Directory()
    report.load_sample_data()

    print '-------------------REPORT 1---------------------'

    for p in report.report1_data():
        print '<Person First Name="%s", Last Name="%s", Gender="%s", Favorite Color="%s", Date of Birth="%d/%d/%d"' % (
            p.first_name,
            p.last_name,
            p.gender,
            p.favorite_color,
            p.date_of_birth.month,
            p.date_of_birth.day,
            p.date_of_birth.year
        )

    print '\n-------------------REPORT 2---------------------'

    for p in report.report2_data():
        print '<Person First Name="%s", Last Name="%s", Gender="%s", Favorite Color="%s", Date of Birth="%d/%d/%d"' % (
            p.first_name,
            p.last_name,
            p.gender,
            p.favorite_color,
            p.date_of_birth.month,
            p.date_of_birth.day,
            p.date_of_birth.year
        )

    print '\n-------------------REPORT 3---------------------'

    for p in report.report3_data():
        print '<Person First Name="%s", Last Name="%s", Gender="%s", Favorite Color="%s", Date of Birth="%d/%d/%d"' % (
            p.first_name,
            p.last_name,
            p.gender,
            p.favorite_color,
            p.date_of_birth.month,
            p.date_of_birth.day,
            p.date_of_birth.year
        )
