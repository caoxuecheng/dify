from flask import current_app
from flask_restful import Resource

from .. import api
from ..auth.oauth import get_oauth_providers


class OAuthLogin2(Resource):
    def get(self):
        oauth_providers = get_oauth_providers()
        with current_app.app_context():
            oauth_provider = oauth_providers.get('casdoor')
        if not oauth_provider:
            return {"error": "Invalid provider"}, 400

        result = {
            'state': 'casdoor',
            'url': oauth_provider.get_authorization_url()

        }
        return result


api.add_resource(OAuthLogin2, "/enterprise/sso/oauth2/login")
