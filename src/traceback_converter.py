import os
import traceback
import json


class TracebackConverter:
    """Tracebackの表示形式を変化するクラス"""

    def __init__(self, e):
        '''
        :param BaseException e:
        '''
        self.e = e

    def get_all(self):
        '''tracebackを一行のJSON形式で取得'''
        
        tb = traceback.extract_tb(self.e.__traceback__)
        tb_list = [
            {
                "file": os.path.basename(frame.filename),
                "line": frame.lineno,
                "function": frame.name,
                "code": frame.line.strip() if frame.line else None,
            }
            for frame in tb
        ]
        error_info = {
            "traceback": tb_list,
            "error_type": type(self.e).__name__,
            "error_message": str(self.e),
        }

        # JSONを一行に変換
        return json.dumps(error_info, separators=(",", ":"))

    def get_origin(self):
        '''エラーの発生源のみ取得し、JSON形式で返却'''
        
        tb = traceback.extract_tb(self.e.__traceback__)
        frame = tb[0]  # 最初のフレームが発生源
        origin_info = {
            "file": os.path.basename(frame.filename),
            "line": frame.lineno,
            "function": frame.name,
            "code": frame.line.strip() if frame.line else None,
            "error_type": type(self.e).__name__,
            "error_message": str(self.e),
        }
        # ここで一行のJSON形式に変換
        return json.dumps(origin_info, separators=(",", ":"))
    