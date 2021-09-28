#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    
   if values is None:       
        values = []
        for nbr in range(10) : 
        a= input("valeur de word 1 : ")
        values.append(a)

    return values.sort()


def anagrams(words: list = None) -> bool:
   
    if words is None :
        words = [input("valeur de word 1 : "),input("valeur de word 1 : ")]
        
    return True if sorted(words[0]) == sorted(words[1]) else False


def contains_doubles(items: list) -> bool:
    
    sorted_items = sorted(items)
    for i in range(1,len(sorted_items) ):
        if sorted_items[i] == sorted_items[i-1]:
            return True

    return False


    return set(items) != len(items)


def average(grades : list) :
    total = 0
    for grade in grades :
        total += grade
    avg = total / len(grades)
    return avg
        

def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    
    #best_student_name=
    best_moy = 0
    best_name = ""

    for name in student_grades :

        moy = sum(student_grades[name]) / len(student_grades[name])
        if moy > best_moy :
            best_moy = moy
            best_name = name

    
    return {best_name: best_moy}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    frequencies = {}
    for letter in sentence :
        if sentence.count(letter) ==x:


    return {}




def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recette = input("nom de la recette : ")
    ingredient =input("ses ingrédients :")
    return {recette : ingredient.split()}


def print_recipe(recipes) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recette = input("nom de la recette : ")

    if recette in recipes :
        print(recette)
    
    
    


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    print(anagrams())


    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
