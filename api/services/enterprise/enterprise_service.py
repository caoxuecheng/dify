

class EnterpriseService:
    @classmethod
    def get_info(cls):
        return {
            "sso_enforced_for_signin": False,
            "sso_enforced_for_signin_protocol": "",
            "sso_enforced_for_web": False,
            "sso_enforced_for_web_protocol": ""
        }
        # return EnterpriseRequest.send_request("GET", "/info")

    @classmethod
    def get_app_web_sso_enabled(cls, app_code):
        return {
            "enabled": True
        }
        # return EnterpriseRequest.send_request("GET", f"/app-sso-setting?appCode={app_code}")
