# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import path

# metadata for font size
font_configs = {
    "catus": {
        "font_name": "Pinyin Catus Sans 1.0",
        "output_font": "Pinyin-Catus-Sans_v1.0.ttf",
        "main_font_path": "WenQuanYiMicroHeiMono-Reduced_fixed.ttf",
        "pinyin_font_path": "LXGWWenKaiMono-Regular.ttf",

        "metadata": {
            "pinyin_canvas": {
                "width": 850,   # ピンイン表示部の幅
                "height": 283.3, # ピンイン表示部の高さ
                "base_line": 935,   # ベースラインからの高さ
                "tracking": 22.145 # 拼音の標準空白幅： Tracking is about uniform spacing across a text selection.
            },
            "expected_hanzi_canvas": {
                "width": 1000, # 基準にする漢字の表示部の幅
                "height": 1000, # 基準にする漢字の表示部の高さ
            },
            # ピンインが 5~6 文字以上(最大は6のはず)のとき、文字が重なることがある。この時にx軸を縮小して重なりを避けるモード
            "is_avoid_overlapping_mode": True, 
            "x_scale_reduction_for_avoid_overlapping": 0.1 # 上記のモードの際に x軸をどれだけ縮小するか
        },
    },
    "tigris": {
        "font_name": "Pinyin Tigris Sans 1.0",
        "output_font": "Pinyin-Tigris-Sans_v1.0.ttf",
        "main_font_path": "WenQuanYiMicroHei-Reduced-Fixed2.ttf",
        "pinyin_font_path": "LXGWWenKaiMono-Regular.ttf",

        "metadata": {
            "pinyin_canvas": {
                "width": 850,   # ピンイン表示部の幅
                "height": 283.3, # ピンイン表示部の高さ
                "base_line": 935,   # ベースラインからの高さ
                "tracking": 22.145 # 拼音の標準空白幅： Tracking is about uniform spacing across a text selection.
            },
            "expected_hanzi_canvas": {
                "width": 1000, # 基準にする漢字の表示部の幅
                "height": 1000, # 基準にする漢字の表示部の高さ
            },
            # ピンインが 5~6 文字以上(最大は6のはず)のとき、文字が重なることがある。この時にx軸を縮小して重なりを避けるモード
            "is_avoid_overlapping_mode": True, 
            "x_scale_reduction_for_avoid_overlapping": 0.1 # 上記のモードの際に x軸をどれだけ縮小するか
        },
    },
    "leo": {
        "font_name": "Pinyin Leo Serif 1.0",
        "output_font": "Pinyin-Leo-Serif_v1.0.ttf",
        "main_font_path": "LXGWWenKaiMono-Regular.ttf",
        "pinyin_font_path": "LXGWWenKaiMono-Regular.ttf",

        "metadata": {
            "pinyin_canvas": {
                "width": 850,   # ピンイン表示部の幅
                "height": 283.3, # ピンイン表示部の高さ
                "base_line": 935,   # ベースラインからの高さ
                "tracking": 22.145 # 拼音の標準空白幅： Tracking is about uniform spacing across a text selection.
            },
            "expected_hanzi_canvas": {
                "width": 1000, # 基準にする漢字の表示部の幅
                "height": 1000, # 基準にする漢字の表示部の高さ
            },
            # ピンインが 5~6 文字以上(最大は6のはず)のとき、文字が重なることがある。この時にx軸を縮小して重なりを避けるモード
            "is_avoid_overlapping_mode": True, 
            "x_scale_reduction_for_avoid_overlapping": 0.1 # 上記のモードの際に x軸をどれだけ縮小するか
        },
    },        
    "onca": {
        "font_name": "Pinyin Onca Handwritten 1.0",
        "output_font": "Pinyin-Onca-Handwritten_v1.0.ttf",
        "main_font_path": "XiaolaiMonoSC-without-Hangul-Regular.ttf",
        "pinyin_font_path": "latin-alpabet-of-SetoFont-SP.ttf",

        "metadata": {
            "pinyin_canvas": {
                "width": 800, # ピンイン表示部の幅
                "height": 300, # ピンイン表示部の高さ
                "base_line": 880, # ベースラインからの高さ
                "tracking": 5 # 拼音の標準空白幅： Tracking is about uniform spacing across a text selection.
            },
            "expected_hanzi_canvas": {
                "width": 1000, # 基準にする漢字の表示部の幅
                "height": 1000, # 基準にする漢字の表示部の高さ
            },
            # ピンインが 5~6 文字以上(最大は6のはず)のとき、文字が重なることがある。この時にx軸を縮小して重なりを避けるモード
            "is_avoid_overlapping_mode": True, 
            "x_scale_reduction_for_avoid_overlapping": 0.1 # 上記のモードの際に x軸をどれだけ縮小するか
        },
    }
}


