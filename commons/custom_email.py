from django.core.mail import send_mail


def send_help_request_email(user_name, is_guest_user, user_email, message):
    message = 'User: '+user_name+'\nEmail: '+user_email+'\nReported a issue in superteacher. \nIssue is: '+message+'\n'
    if is_guest_user:
        message += 'The user is a guest user'

    send_mail(
        subject='User Reported an Issue in Superteacher',
        message=message,
        recipient_list=['Studykitco@gmail.com', 'info@superteacher.pk'],
        fail_silently=False,
    )
