import os
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
class Actions:
    INIT = "INIT"
    CHECK_CONFIG_FILES = "CHECK_CONFIG_FILES"
    SAVE_IMAGE_REBUILD_CONFIG_FILE = "SAVE_IMAGE_REBUILD_CONFIG_FILE"
    NOTIFY = "NOTIFY"
    IMMUTABLE_IMAGE_BUILD = "IMMUTABLE_IMAGE_BUILD"
    MUTABLE_IMAGE_BUILD = "MUTABLE_IMAGE_BUILD"
    VM_REFRESH = "VM_REFRESH"
class BQ:
    def __init__(self, env, credentials=None):
        pass
class LOG:
    @staticmethod
    def info(msg):
        print(f"[INFO] {msg}")
class Stage3ImageRebuild(object):
    def __init__(self, step=Actions.IMMUTABLE_IMAGE_BUILD, status="RUNNING", credentials=None):
        self.step = step
        self.status = status
        self.env = os.getenv("gcp_env", "dev")
        self.config_file = "image_rebuild_config.json"
        self.credentials = credentials
        self._db = BQ(self.env, credentials=credentials)
        self.workdir = os.getenv("WORKSPACE", ".")
        self.cur_sa = os.getenv("current_service_account", "")
        self.build_user = os.getenv("BUILD_USER", "")
        self.build_user_id = os.getenv("BUILD_USER_ID", "")
        self.log_level = os.getenv("log_level", "Info")
        self.image_rollback_to = os.getenv("target_image_name_for_rollback", "")
        self.conf = {}
        self.action = os.getenv("action", "")
        
        if self.cur_sa.startswith("gce-stage3-image-builder@hsbc-9940998-hkihubhk-"):
            self.location = "HK"
        else:
            self.location = "UK"
            
        LOG.info(f"current Jenkins is in {self.location}")

    def init(self):
        LOG.info("Initializing system contexts...")

    def check_config_files(self):
        target_path = os.path.join(self.workdir, self.config_file)
        LOG.info(f"Checking target tracking asset array configuration path: {target_path}")

    def save_image_rebuild_config_file(self):
        LOG.info("Saving configurations down to pipeline datastore targets...")

    def notify(self):
        LOG.info("Sending notifications to standard messaging groups...")

    def immutable_image_build(self):
        LOG.info("Running immutable image build tracking process...")

    def mutable_image_build(self):
        LOG.info("Running standard mutable configuration routines...")

    def run(self):
        if self.step == Actions.INIT:
            self.init()
        elif self.step == Actions.CHECK_CONFIG_FILES:
            self.check_config_files()
        elif self.step == Actions.SAVE_IMAGE_REBUILD_CONFIG_FILE:
            self.save_image_rebuild_config_file()
        elif self.step == Actions.NOTIFY:
            self.notify()
        elif self.step == Actions.IMMUTABLE_IMAGE_BUILD:
            self.immutable_image_build()
        elif self.step == Actions.MUTABLE_IMAGE_BUILD:
            self.mutable_image_build()
if __name__ == "__main__":
    runner = Stage3ImageRebuild()
    runner.run()
