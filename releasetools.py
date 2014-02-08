# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2012 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom OTA Package commands for honami"""

import os

TARGET_DIR = os.getenv('OUT')

def FullOTA_Assertions(self):
  self.output_zip.write(os.path.join(TARGET_DIR, "c6902.sh"), "c6902.sh")
  self.script.AppendExtra('package_extract_file("c6902.sh", "/tmp/c6902.sh");')
  self.script.AppendExtra('set_perm(0, 0, 0777, "/tmp/c6902.sh");')
  self.script.AppendExtra('run_program("/tmp/c6902.sh");')
