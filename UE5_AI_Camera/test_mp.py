try:
    # 我们不找 mp.solutions 了，直接强行进入它老家拿东西
    import mediapipe.python.solutions.hands as mp_hands
    print("✅ 完美成功！这说明库没坏，只是名字没暴露出来！")
except Exception as e:
    print("❌ 抓到真凶了！隐藏在背后的真正报错是：\n", e)