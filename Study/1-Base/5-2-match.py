# ============= match - альтернатива if/else ==============

score = 85

match score:
    case s if s >= 90:
        print('Rating: Excellent')
    case s if s >= 75:
        print('Rating: Good')
    case s if s >= 60:
        print('Rating: Satisfactory')
    case _:
        print('Test not passed')
