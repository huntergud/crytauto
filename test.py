import pyupbit

access = "sB316qvqcPQ9T2E94fMjN05Tm1qWPPWMoxuhuRRE"          # 본인 값으로 변경
secret = "tRi9PYxE8kKoCXigLYJ05ixpQFNJQLdGhzPTlk7R"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW"))     # 보유 현금 조회
print(upbit.get_balance("KRW-DOGE"))        # 보유 도지코인 조회
print(upbit.get_balance("KRW-TRX"))         # 보유 비트코인 조회
print(upbit.get_balance("KRW-XRP"))         # 보유 이더리움 조회
