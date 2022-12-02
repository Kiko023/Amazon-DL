import logging, subprocess, re, base64
from tqdm import tqdm
from pyamazon.Decrypt.cdm import cdm, deviceconfig
import os
import subprocess

currentFile = __file__
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)
wv_cvt = dirPath + "\\wv_cvt.exe"
original_license_request_path = dirPath + "\\req_test.bin"
#modded_license_reqresp_path = dirPath + "\\TempFile_2209"
original_license_response_path = dirPath + "\\lic_res.b64"

class WvDecrypt(object):
    WV_SYSTEM_ID = [
     237, 239, 139, 169, 121, 214, 74, 206, 163, 200, 39, 220, 213, 29, 33, 237]

    def __init__(self, init_data_b64, cert_data_b64):
        self.init_data_b64 = init_data_b64
        self.cert_data_b64 = cert_data_b64
        self.cdm = cdm.Cdm()

        def check_pssh(pssh_b64):
            pssh = base64.b64decode(pssh_b64)
            if not pssh[12:28] == bytes(self.WV_SYSTEM_ID):
                new_pssh = bytearray([0, 0, 0])
                new_pssh.append(32 + len(pssh))
                new_pssh[4:] = bytearray(b'pssh')
                new_pssh[8:] = [0, 0, 0, 0]
                new_pssh[13:] = self.WV_SYSTEM_ID
                new_pssh[29:] = [0, 0, 0, 0]
                new_pssh[31] = len(pssh)
                new_pssh[32:] = pssh
                return base64.b64encode(new_pssh)
            else:
                return pssh_b64

        self.session = self.cdm.open_session(check_pssh(self.init_data_b64),
                                             deviceconfig.DeviceConfig(deviceconfig.device_chromecdm_2449))
        if self.cert_data_b64:
            self.cdm.set_service_certificate(self.session, self.cert_data_b64)

    def log_message(self, msg):
        return ('{}').format(msg)

    def start_process(self):
        keyswvdecrypt = []
        try:
            for key in self.cdm.get_keys(self.session):
                if key.type == 'CONTENT':
                    keyswvdecrypt.append(self.log_message(('{}:{}').format(key.kid.hex(), key.key.hex())))

        except Exception:
            return (
             False, keyswvdecrypt)

        return (
         True, keyswvdecrypt)

    def get_challenge(self):
        original_chellenge = self.cdm.get_license_request(self.session)
        with open(original_license_request_path, "wb") as f:
            f.write(base64.b64encode(original_chellenge))
            f.close()
        subprocess.run([wv_cvt, original_license_request_path])
        with open("TempFile_2209", "rb") as f:
            modded_challenge = base64.b64decode(f.read())
            f.close()
        return modded_challenge

    def update_license(self, license_b64):
        with open(original_license_response_path, "w") as f:
            f.write(license_b64)
            f.close()
        subprocess.run([wv_cvt, original_license_response_path])
        with open("TempFile_2209", "rb") as f:
            modded_license = f.read()
            f.close()
        self.cdm.provide_license(self.session, modded_license)
        return True