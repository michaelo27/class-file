class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age =age
        self.tracks = tracks
        self.score = score
    def Students_data(self):
        print(self.name,self.age,self.tracks,self.score )

    new_name = 'Peter'
    new_age = "34"
    new_track="UI/UX"
    new_score = 45.90

    @classmethod
    def change_name(cls,newName):
        cls.new_name = newName

    @classmethod
    def change_age(cls,newAge):
        cls.new_age = newAge

    
    @classmethod
    def add_track(cls,newTrack):
        cls.new_track = newTrack

    
    @classmethod
    def get_score(cls,newScore):
        cls.new_score = newScore
        return newScore


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Peter = Student(name="Peter", age=34, tracks="UI/UX",score=45.90)

Bob.Students_data()
Peter.Students_data()
Student.add_track("UI/UX")
Student.change_age(34)
Student.change_name("Peter")
Student.get_score(newScore="")
