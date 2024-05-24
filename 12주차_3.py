import pickle

filepath = 'data/example.bin'              # 데이터파일에 대한 파일경로명

def save_data(num, name, height, scores):  # 피클링하여 저장
    with open(filepath, 'wb') as file:
        pickle.dump(num, file)
        pickle.dump(name, file)
        pickle.dump(height, file)
        pickle.dump(scores, file)

def load_data():
    with open(filepath, 'rb') as file:     # 언파클링해 반환
        num = pickle.load(file)
        name = pickle.load(file)
        height = pickle.load(file)
        scores = pickle.load(file)

    return num, name, height, scores       # 튜플로 반환

num, name, height = 123, '홍길동', 180.5
scores = {'mid': 90, 'fin': 95, 'rep': 10, 'att': 10}

save_data(num, name, height, scores)

r_num, r_name, r_height, r_scores = load_data()

print(r_num)
print(r_name)
print(r_height)
print(r_scores)
