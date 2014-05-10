def intercom_custom_data(request):
    try:
        if request.user.is_authenticated():
            poet = request.user.get_profile()
            return {
                "intercom_user_id": poet.pk,
                "intercom_name": poet.name,
                "intercom_premium_user": poet.premium_user,
                "intercom_num_drafts": poet.poem_set.filter(is_draft=True).count(),
                "intercom_num_published_poems": poet.poem_set.filter(is_draft=False).count(),
                "intercom_num_revisions": poet.poemrevision_set.filter().count(),
                "intercom_num_reads": poet.read_set.count(),
                "intercom_num_fantastics": poet.fantastic_set.count(),
                "intercom_widget": {
                    "activator": "#Intercom"
                },
            }
    except:
        pass

    return {}
