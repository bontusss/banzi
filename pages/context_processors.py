from users.models import Profile


def get_profile_type(request):
    """
    context processor must return a dictionary.
    This method returns if the User.Profile.type is either "Employer" or "Candidate".
    """
    # current_user = request.user
    # if current_user:
    #     pro = Profile.objects.filter(user=current_user)
    
    # other details
    site_name = 'Banzi'
    site_description = 'Find Tech jobs around you.'
    email = "support@banzi.com"
    phone = "+2348118773038"
    return {
        # 'pro': pro,
        'site_name': site_name,
        'description': site_description,
        'email': email,
        'phone': phone,
    }
