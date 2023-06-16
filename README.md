# Parte prática da prova 2 do módulo 6 de Engenharia de Computação

## explicação

Fundamentos
A detecção de objetos usando classificadores em cascata baseados em recursos Haar é um método eficaz de detecção de objetos proposto por Paul Viola e Michael Jones em seu artigo, “Rapid Object Detection using a Boosted Cascade of Simple Features” em 2001. É uma abordagem baseada em aprendizado de máquina em que um A função cascata é treinada a partir de muitas imagens positivas e negativas. Em seguida, é usado para detectar objetos em outras imagens.

Aqui vamos trabalhar com detecção de rosto. Inicialmente, o algoritmo precisa de muitas imagens positivas (imagens de rostos) e imagens negativas (imagens sem rostos) para treinar o classificador. Em seguida, precisamos extrair recursos dele. Para isso, são usados ​​os recursos haar mostrados na imagem abaixo. Eles são como nosso kernel convolucional. Cada recurso é um valor único obtido pela subtração da soma dos pixels sob o retângulo branco da soma dos pixels sob o retângulo preto.

Recursos de Haar
Agora, todos os tamanhos e localizações possíveis de cada kernel são usados ​​para calcular muitos recursos. (Imagine quanta computação ele precisa? Mesmo uma janela de 24x24 resulta em mais de 160.000 recursos). Para cada cálculo de recurso, precisamos encontrar a soma dos pixels sob os retângulos branco e preto. Para resolver isso, eles introduziram as imagens integrais. Simplifica o cálculo da soma de pixels, quão grande pode ser o número de pixels, para uma operação envolvendo apenas quatro pixels. Legal, não é? Isso torna as coisas super-rápidas.

Mas entre todas essas características que calculamos, a maioria delas é irrelevante. Por exemplo, considere a imagem abaixo. A linha superior mostra dois bons recursos. A primeira característica selecionada parece focar na propriedade de que a região dos olhos costuma ser mais escura que a região do nariz e das bochechas. A segunda característica selecionada depende da propriedade de que os olhos são mais escuros do que a ponte do nariz. Mas as mesmas janelas aplicadas nas bochechas ou em qualquer outro lugar são irrelevantes. Então, como selecionamos os melhores recursos entre mais de 160.000 recursos? É alcançado por Adaboost .

Detecção de rosto
Para isso, aplicamos cada recurso em todas as imagens de treinamento. Para cada feição, encontra o melhor limiar que classificará as faces em positivas e negativas. Mas, obviamente, haverá erros ou classificações incorretas. Selecionamos as feições com taxa mínima de erro, ou seja, são as feições que melhor classificam as imagens faciais e não faciais. (O processo não é tão simples assim. Cada imagem recebe um peso igual no início. Após cada classificação, os pesos das imagens mal classificadas são aumentados. Em seguida, novamente o mesmo processo é feito. Novas taxas de erro são calculadas. Também novos pesos. Os o processo é continuado até que a precisão necessária ou a taxa de erro seja alcançada ou o número necessário de recursos seja encontrado).

O classificador final é uma soma ponderada desses classificadores fracos. É chamado de fraco porque sozinho não consegue classificar a imagem, mas junto com outros forma um classificador forte. O jornal diz que até 200 recursos fornecem detecção com 95% de precisão. Sua configuração final tinha cerca de 6.000 recursos. (Imagine uma redução de mais de 160.000 recursos para 6.000 recursos. Isso é um grande ganho).

Então agora você tira uma imagem. Pegue cada janela de 24x24. Aplique 6000 recursos a ele. Verifique se é rosto ou não. Uau.. Uau.. Não é um pouco ineficiente e demorado? É sim. Os autores têm uma boa solução para isso.

Em uma imagem, a maior parte da região da imagem é uma região não facial. Portanto, é melhor ter um método simples para verificar se uma janela não é uma região de face. Se não estiver, descarte-o de uma só vez. Não processe novamente. Em vez disso, concentre-se na região onde pode haver um rosto. Assim, podemos encontrar mais tempo para verificar uma possível região do rosto.

Para isso introduziram o conceito de Cascata de Classificadores . Em vez de aplicar todos os 6000 recursos em uma janela, agrupe os recursos em diferentes estágios de classificadores e aplique um por um. (Normalmente, os primeiros estágios conterão um número muito menor de recursos). Se uma janela falhar no primeiro estágio, descarte-a. Não consideramos os recursos restantes nele. Se passar, aplique a segunda etapa de recursos e continue o processo. A janela que passa por todos os estágios é uma região de face. Como é o plano!!!

O detector dos autores tinha mais de 6.000 recursos com 38 estágios com 1, 10, 25, 25 e 50 recursos nos primeiros cinco estágios. (Dois recursos na imagem acima são realmente obtidos como os dois melhores recursos do Adaboost). De acordo com os autores, em média, 10 recursos em mais de 6.000 são avaliados por subjanela.

Portanto, esta é uma explicação intuitiva simples de como funciona a detecção de rosto Viola-Jones. Leia o artigo para obter mais detalhes ou verifique as referências na seção Recursos adicionais.

Detecção Haar-cascade no OpenCV
O OpenCV vem com um treinador e um detector. Se você deseja treinar seu próprio classificador para qualquer objeto, como carro, avião, etc., pode usar o OpenCV para criar um. Seus detalhes completos são fornecidos aqui: Cascade Classifier Training.

Aqui vamos lidar com a detecção. O OpenCV já contém muitos classificadores pré-treinados para face, olhos, sorriso, etc. Esses arquivos XML são armazenados na opencv/data/haarcascades/pasta. Vamos criar um detector facial e ocular com o OpenCV.

Primeiro, precisamos carregar os classificadores XML necessários. Em seguida, carregue nossa imagem de entrada (ou vídeo) no modo de escala de cinza.

Agora encontramos os rostos na imagem. Se faces forem encontradas, ele retornará as posições das faces detectadas como Rect(x,y,w,h). Depois de obter esses locais, podemos criar um ROI para o rosto e aplicar a detecção de olhos nesse ROI (já que os olhos estão sempre no rosto !!!).

