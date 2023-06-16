# Parte prática da prova 2 do módulo 6 de Engenharia de Computação

## explicação

No exercício foi utilizada a detecção de faces com classificadores em cascatas (haar cascate que sua função é treinada a partir de muitas imagens positivas e negativas e depois é usada para detectar objetos em outras imagens)

Assim, o OpenCV vem com um treinador e um detector, assim o openCV já contém muitos classificadores pré-treinados para face, olhos, sorriso... ou seja no main.py carregamos os classificadores XML necessários, em seguida o vídeo de entrada é carregado e nele é implementado o modo de escala de cinza, encontramos os rostos no video, assim se as faces forem encontradas, ele retornará as posições das faces detectadas como Rect(x,y,w,h). 
