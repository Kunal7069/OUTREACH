import dropbox
from uuid import uuid4
from fastapi import UploadFile
from datetime import datetime

# ACCESS_TOKEN = "sl.u.AFwrP424jes71TuHQbrUx_JJLXQhZAzjubdwsxqS4fRcrU7A3cE9rdqeKrS2WHfRDuuVnyHIT_xIN0_o1R71Mkms7j5BbBBYmCrNR5hk7TEsTzlbq3CbQpbN-pCZkQ0cIjsQYAVUgJ-4p9XLsHhn4PTgyWovhB8JcsEuELz0KMqmMlh2WMHMMfnmaeF4ZKAHM84xBPXGRBAhW7rQiU61OT6RlDhFhkboCvsLrnsMegq5bomZjVKzgamWIFYqBFuafSaSBE3Zdr26eAshVIX_7zTQDxzECgEWleLaLzhvq13_nSgBf1PwtuoJLd-te5Cyty6MWPXB0AMplTztVuu4xrpVM7_KvSLA6N7IwZBY368ZsagY974lVkc6Wysd-2pRnaBvCly_In3NRb2i8T752z8ZADQNUv8pqYrp1GT61Py5XEQ7uYpaCT1ZP-IJCG5B0QRR1YUdIrpl2PaFKRxCHe3ABPge6jLPNC52I9jOMEinRFOqDDQc5rFWxrGgfi5C9-ORTLVPyoaNyskxcLpPMlNukbZYepRwSjvCwZmOsaRjSDI9vWWRsAKr_CUksTNGdtfI_oI_n1ydydtkKUsLDS2213vFz2ReSjWa-nyGU_9lT6UvbLhKhg0K36eeWMbOHYCYsrOGF0LV_SIf-rfx9RsYueLopxkV9UJxidA3gbKtBpyT7_w_F3Pya5-HQsM3dJKNUtjTNWzPbMTuQznxrKACMxhVEtRAQDZAT36YJRmo0FYiWM_0YIGjSYgt8UeX5U8RYWtUBLcT5vyWchojiOEzmmTZm_-RDpLi5uurTMRc6-V1jUi0AApTitgbQMC2Vj4eFdlEv2kFTFPTJBGBaLm8nL8aBYSXb6lwtRXyjcpVn6BaiHJYk1Aec3LUik1ptpZEe2gszYoKylx38RtS95VzOY2gTrLgb2FH9zJfb7V_JGqZWEXGM-f7UGC1Ab8-oR23zAlEnbAxrAbzsQJu0Hgc4vtSuluSq0-iLDY4NdgSgvzNY7Ui0KuyIHX1nkZTygVvjh32eDWKtMgbjL7Q0ZeR7y-EHcTXHSxSmWrRMQ3wI0EbcGmstfKW31mODaCrjX6ScriiAMKxkEzwvO--uVcah2oJQxUvQ8Xam-V-_o5bOt0ojLDSz3hGhZZR--DaiQArvLB4AaLGSDUC8WN1L0MLpcrqAJRQ83ETZyijIiHkxPlwT2QMehM9FlUCioWmRnTNs4DMxxdNh1PJS7ucykkvKPTnMj5u07-cfx6WFt2FuEgmr-zHArultq-6ksE4SIuRvwSipBc4J6qwnNFczskhpOLmieihMYfxETYdT1c0lkUdSemNLRO5bEserH423EyIH0eFRYq-jf5--gpkyjKQZGLGZzY76vgMC4sKgLS0JaxO8p3fFd5nxfYiY2NpST7ffQycm1LSAm2lr8zJL9_8Rxpqns_JotP_GNogOaWJZMuBziRq42FsK56bd4J6QZU"

APP_KEY = "831rhakm1chm136"
APP_SECRET = "3litvdoqd1djj3c"
REFRESH_TOKEN = "gIMBpRQXtWIAAAAAAAAAAT0I5URJeczB7LA0YgNRSHcjZcZBaYaczbfJRT--hjPU"

def upload_to_dropbox(userid:str,file: UploadFile, tag: str = "untagged") -> str:
    # dbx = dropbox.Dropbox(ACCESS_TOKEN)
    dbx = dropbox.Dropbox(
        app_key=APP_KEY,
        app_secret=APP_SECRET,
        oauth2_refresh_token=REFRESH_TOKEN
    )
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{userid}_{tag}_{timestamp}.pdf"
    dropbox_path = f"/{filename}"

    # Read file contents and upload
    file_bytes = file.file.read()
    dbx.files_upload(file_bytes, dropbox_path, mode=dropbox.files.WriteMode("overwrite"))

    # Create shared link
    shared_link_metadata = dbx.sharing_create_shared_link_with_settings(dropbox_path)
    url = shared_link_metadata.url.replace("?dl=0", "?dl=1")
    return url