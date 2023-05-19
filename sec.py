add more rss feeds here: import feedparser
import time
import smtplib

# Define the list of RSS feeds to check.
feeds = [
    "https://cve.mitre.org/about/rss.xml",
    "https://nvd.nist.gov/feeds/xml/cve/recent.xml",
    "https://owasp.org/www-project-news/rss.xml",
]

# Define the email address to send the report to.
email_address = "your@email.address"

# Define the password for the email account.
email_password = "your_password"

# Define the subject line for the report.
subject_line = "Cybersecurity Incident Report"

# Define the body of the report.
report_body = """
This is a report of the latest cybersecurity incidents.

* CVE-2023-0123 - A vulnerability has been discovered in the Linux kernel that could allow an attacker to take control of the system.
* CVSS score: 10.0
* NIST severity: Critical
* OWASP risk: High

* CVE-2023-0456 - A vulnerability has been discovered in the Apache web server that could allow an attacker to execute arbitrary code.
* CVSS score: 9.0
* NIST severity: High
* OWASP risk: Critical

* CVE-2023-0789 - A vulnerability has been discovered in the Microsoft Windows operating system that could allow an attacker to gain unauthorized access.
* CVSS score: 8.0
* NIST severity: Important
* OWASP risk: Medium

Please take the necessary steps to protect your systems from these vulnerabilities.
"""

# Create a new email message.
message = smtplib.MIMEMultipart()
message["From"] = email_address
message["To"] = email_address
message["Subject"] = subject_line
message.attach(MIMEText(report_body, "plain"))

# Send the email message.
smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.starttls()
smtp.login(email_address, email_password)
smtp.sendmail(email_address, email_address, message.as_string())
smtp.quit()

# Check the RSS feeds every 5 minutes.
while True:
    for feed in feeds:
        feed_data = feedparser.parse(feed)
        for entry in feed_data.entries:
            if entry.title not in report_body:
                report_body += f"* {entry.title} - {entry.link}\n"

    time.sleep(300)

    # Send the report email daily.
    time.sleep(86400)
