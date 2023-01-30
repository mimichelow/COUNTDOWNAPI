from flask import Flask, jsonify, request
import json
import countdownSolver as cs
import countdownNumberSolver as cns

app = Flask(__name__)


@app.route("/api/letters", methods=['GET'])
def letters():
    letter = request.args.get("letter")
    if not str.isalpha(letter):
        return {}, 400
    return jsonify(cs.countdownSolver(letter)), 200


@app.route("/api/numbers", methods=['GET'])
def numbers():
    target = request.args.get("target")
    nums = request.args.get("nums")
    nums = nums.split(",")
    if not checkArgs(target, nums):
        return {"response": None}, 400
    else:
        temp = [int(n) for n in nums]
        return cns.countdownNumerSolver(numbers=temp, target=int(target)), 200


def checkArgs(t, n):
    if t.isnumeric():
        if len(t) == 3:
            for num in n:
                if not num.isnumeric():
                    return False
            return True
        return False
    else:
        return False


if __name__ == '__main__':
    app.run()
