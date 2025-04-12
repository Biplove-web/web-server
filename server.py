from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow JS frontend to talk to this backend

# Simulated data
result_db = {
  "1000": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Nepali",
      "gpa": "3.6",
      "grade": "A"
    }
  ],
  "1001": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "English",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1002": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1003": [
    {
      "subject": "Mathematics",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1004": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1005": [
    {
      "subject": "Mathematics",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1006": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1007": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1008": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "English",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1009": [
    {
      "subject": "Mathematics",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.6",
      "grade": "D+"
    }
  ],
  "1010": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.6",
      "grade": "D+"
    }
  ],
  "1011": [
    {
      "subject": "Mathematics",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Science",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1012": [
    {
      "subject": "Mathematics",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Science",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "English",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1013": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1014": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "English",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1015": [
    {
      "subject": "Mathematics",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.6",
      "grade": "D+"
    }
  ],
  "1016": [
    {
      "subject": "Mathematics",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1017": [
    {
      "subject": "Mathematics",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.6",
      "grade": "D+"
    }
  ],
  "1018": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1019": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1020": [
    {
      "subject": "Mathematics",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1021": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1022": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "3.2",
      "grade": "B+"
    }
  ],
  "1023": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1024": [
    {
      "subject": "Mathematics",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1025": [
    {
      "subject": "Mathematics",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1026": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1027": [
    {
      "subject": "Mathematics",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1028": [
    {
      "subject": "Mathematics",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1029": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1030": [
    {
      "subject": "Mathematics",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Science",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Nepali",
      "gpa": "3.6",
      "grade": "A"
    }
  ],
  "1031": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "English",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1032": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1033": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1034": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1035": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "3.2",
      "grade": "B+"
    }
  ],
  "1036": [
    {
      "subject": "Mathematics",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "3.2",
      "grade": "B+"
    }
  ],
  "1037": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1038": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1039": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Nepali",
      "gpa": "3.6",
      "grade": "A"
    }
  ],
  "1040": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1041": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1042": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1043": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "3.6",
      "grade": "A"
    }
  ],
  "1044": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1045": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1046": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "English",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Social Studies",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1047": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1048": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Nepali",
      "gpa": "3.2",
      "grade": "B+"
    }
  ],
  "1049": [
    {
      "subject": "Mathematics",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1050": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1051": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1052": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1053": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "English",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "3.2",
      "grade": "B+"
    }
  ],
  "1054": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1055": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1056": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1057": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Social Studies",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1058": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1059": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1060": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Nepali",
      "gpa": "1.6",
      "grade": "D+"
    }
  ],
  "1061": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Nepali",
      "gpa": "3.2",
      "grade": "B+"
    }
  ],
  "1062": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1063": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "3.2",
      "grade": "B+"
    }
  ],
  "1064": [
    {
      "subject": "Mathematics",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1065": [
    {
      "subject": "Mathematics",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Science",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "3.6",
      "grade": "A"
    }
  ],
  "1066": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1067": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1068": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1069": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1070": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "3.2",
      "grade": "B+"
    }
  ],
  "1071": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1072": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1073": [
    {
      "subject": "Mathematics",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1074": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "English",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1075": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "English",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1076": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1077": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Social Studies",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.0",
      "grade": "C"
    }
  ],
  "1078": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1079": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1080": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1081": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1082": [
    {
      "subject": "Mathematics",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "3.2",
      "grade": "B+"
    }
  ],
  "1083": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1084": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1085": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1086": [
    {
      "subject": "Mathematics",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Science",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "English",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1087": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "English",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Social Studies",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1088": [
    {
      "subject": "Mathematics",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Science",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1089": [
    {
      "subject": "Mathematics",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Science",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "English",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "1.6",
      "grade": "D+"
    }
  ],
  "1090": [
    {
      "subject": "Mathematics",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Science",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "English",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Social Studies",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Nepali",
      "gpa": "0.8",
      "grade": "E"
    }
  ],
  "1091": [
    {
      "subject": "Mathematics",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Social Studies",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1092": [
    {
      "subject": "Mathematics",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1093": [
    {
      "subject": "Mathematics",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Science",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "English",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "2.4",
      "grade": "C+"
    }
  ],
  "1094": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "0.8",
      "grade": "E"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1095": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ],
  "1096": [
    {
      "subject": "Mathematics",
      "gpa": "1.2",
      "grade": "D"
    },
    {
      "subject": "Science",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "English",
      "gpa": "3.2",
      "grade": "B+"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "1.2",
      "grade": "D"
    }
  ],
  "1097": [
    {
      "subject": "Mathematics",
      "gpa": "1.6",
      "grade": "D+"
    },
    {
      "subject": "Science",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "English",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.4",
      "grade": "C+"
    },
    {
      "subject": "Nepali",
      "gpa": "1.6",
      "grade": "D+"
    }
  ],
  "1098": [
    {
      "subject": "Mathematics",
      "gpa": "4.0",
      "grade": "A+"
    },
    {
      "subject": "Science",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "English",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Social Studies",
      "gpa": "2.8",
      "grade": "B"
    },
    {
      "subject": "Nepali",
      "gpa": "2.8",
      "grade": "B"
    }
  ],
  "1099": [
    {
      "subject": "Mathematics",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Science",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "English",
      "gpa": "2.0",
      "grade": "C"
    },
    {
      "subject": "Social Studies",
      "gpa": "3.6",
      "grade": "A"
    },
    {
      "subject": "Nepali",
      "gpa": "4.0",
      "grade": "A+"
    }
  ]
}


@app.route('/get_result', methods=['POST'])
def get_result():
    data = request.json
    student_id = data.get('id')

    if student_id in result_db:
        return jsonify(result_db[student_id])
    else:
        return jsonify({"error": "ID not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
