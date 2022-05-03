import os
import codecs
import argparse
import model
import glob
from utils import get_logger

LOG = get_logger(__name__)

def read_file(file_name):
    LOG.info('Reading %s' % file_name)
    sents = []
    f = codecs.open(file_name, 'r', 'utf-8')
    for line in f:
        line = line.strip()
        if len(line.split('\t')) == 2:
            sent_id, sent = line.split('\t')
            words = []
            for word in sent.split():
                if word != '':
                    words.append(word)
            sents.append(' '.join(words))
    return sents

def align_file(file1, file2, model_name, gold,layernumber):
    # Model
    if model_name == 'simalign-argmax':
        aligner = model.Simalign(matching_methods='a',layer=layernumber)
    elif model_name == 'simalign-itermax':
        aligner = model.Simalign(matching_methods='i',layer=layernumber)
    elif model_name == 'eflomal':
        aligner = model.Eflomal()
    elif model_name == 'fastalign':
        aligner = model.Fastalign()



    # Read data
    source_sentences = read_file(file1)
    target_sentences = read_file(file2)
    gs = read_file(gold)
    
    # Word Alignment
    aligns = aligner.align_sentences(source_sentences, target_sentences)

    # Evaluation
    pred_num, gold_num, correct_num_p, correct_num_r = 0, 0, 0, 0
    for align, g in zip(aligns, gs):
        g_items = g.strip().split()
        gold_num += len([edge for edge in g_items if '-' in edge])
        for edge in align.strip().split():
            pred_num += 1
            element1 = int(edge.split('-')[0])
            element2 = int(edge.split('-')[1])
            if edge in g_items or '%sp%s' % (element1, element2) in g_items:
                correct_num_p += 1
            if edge in g_items:
                correct_num_r += 1
    global f1
    global prec
    global rec
    global aer
    prec = correct_num_p / pred_num
    rec = correct_num_r / gold_num
    f1 = 2 * prec * rec / (prec + rec)
    aer = 1 - (correct_num_p + correct_num_r) / (pred_num + gold_num)
    LOG.info('Prec %.3f; Rec %.3f; F1 %.3f; AER %.3f.' % (prec, rec, f1, aer))



if __name__ == '__main__':
    f1_matrix=[]
    prec_matrix=[]
    rec_matrix=[]
    aer_matrix=[]
    path='data'
    list=os.listdir(path)
    a=range(13)

for j in a:
    layernumber=j
    for i in list:
        if i =='eng_ces' :
            file1 = 'data/eng_ces/eng_gold.txt'
            file2 = 'data/eng_ces/ces_gold.txt'
            gold = 'data/eng_ces/eng_ces.gold'
            align_file(file1, file2, 'simalign-itermax', gold,layernumber)
            f1_matrix.append(str(f1))
            f1_matrix.append('/')
            prec_matrix.append(str(prec))
            prec_matrix.append('/')
            rec_matrix.append(str(rec))
            rec_matrix.append('/')
            aer_matrix.append(str(aer))
            aer_matrix.append('/')
        elif i == 'eng_deu':
            file1 = 'data/eng_deu/eng_gold.txt'
            file2 = 'data/eng_deu/deu_gold.txt'
            gold = 'data/eng_deu/eng_deu.gold'
            align_file(file1, file2, 'simalign-itermax', gold,layernumber)
            f1_matrix.append(str(f1))
            f1_matrix.append('/')
            prec_matrix.append(str(prec))
            prec_matrix.append('/')
            rec_matrix.append(str(rec))
            rec_matrix.append('/')
            aer_matrix.append(str(aer))
            aer_matrix.append('/')
        elif i == 'eng_fas':
            file1 = 'data/eng_fas/eng_gold.txt'
            file2 = 'data/eng_fas/fas_gold.txt'
            gold = 'data/eng_fas/eng_fas.gold'
            align_file(file1, file2, 'simalign-itermax', gold,layernumber)
            f1_matrix.append(str(f1))
            f1_matrix.append('/')
            prec_matrix.append(str(prec))
            prec_matrix.append('/')
            rec_matrix.append(str(rec))
            rec_matrix.append('/')
            aer_matrix.append(str(aer))
            aer_matrix.append('/')
        elif i=='eng_fra':
            file1 = 'data/eng_fra/eng_bible_gold.txt'
            file2 = 'data/eng_fra/fra_bible_gold.txt'
            gold = 'data/eng_fra/eng_fra_bible.gold'
            align_file(file1, file2, 'simalign-itermax', gold,layernumber)
            f1_matrix.append(str(f1))
            f1_matrix.append('/')
            prec_matrix.append(str(prec))
            prec_matrix.append('/')
            rec_matrix.append(str(rec))
            rec_matrix.append('/')
            aer_matrix.append(str(aer))
            aer_matrix.append('/')
        elif i=='eng_fra2':
            file1 = 'data/eng_fra2/eng_hans_gold.txt'
            file2 = 'data/eng_fra2/fra_hans_gold.txt'
            gold = 'data/eng_fra2/eng_fra_hans.gold'
            align_file(file1, file2, 'simalign-itermax', gold,layernumber)
            f1_matrix.append(str(f1))
            f1_matrix.append('/')
            prec_matrix.append(str(prec))
            prec_matrix.append('/')
            rec_matrix.append(str(rec))
            rec_matrix.append('/')
            aer_matrix.append(str(aer))
            aer_matrix.append('/')
        elif i=='eng_hin' :
            file1 = 'data/eng_hin/eng_gold.txt'
            file2 = 'data/eng_hin/hin_gold.txt'
            gold = 'data/eng_hin/eng_hin.gold'
            align_file(file1, file2, 'simalign-itermax', gold,layernumber)
            f1_matrix.append(str(f1))
            f1_matrix.append('/')
            prec_matrix.append(str(prec))
            prec_matrix.append('/')
            rec_matrix.append(str(rec))
            rec_matrix.append('/')
            aer_matrix.append(str(aer))
            aer_matrix.append('/')
        elif i=='eng_ron':
            file1 = 'data/eng_ron/eng_03_gold.txt'
            file2 = 'data/eng_ron/ron_03_gold.txt'
            gold = 'data/eng_ron/eng_03_ron.gold'
            align_file(file1, file2, 'simalign-itermax', gold,layernumber)
            f1_matrix.append(str(f1))
            f1_matrix.append('/')
            prec_matrix.append(str(prec))
            prec_matrix.append('/')
            rec_matrix.append(str(rec))
            rec_matrix.append('/')
            aer_matrix.append(str(aer))
            aer_matrix.append('/')
        elif i=='eng_ron2':
            file1 = 'data/eng_ron2/eng_05_gold.txt'
            file2 = 'data/eng_ron2/ron_05_gold.txt'
            gold = 'data/eng_ron2/eng_05_ron.gold'
            align_file(file1, file2, 'simalign-itermax', gold,layernumber)
            f1_matrix.append(str(f1))
            f1_matrix.append('/')
            prec_matrix.append(str(prec))
            prec_matrix.append('/')
            rec_matrix.append(str(rec))
            rec_matrix.append('/')
            aer_matrix.append(str(aer))
            aer_matrix.append('/')
        elif i=='fin_grc':
            file1 = 'data/fin_grc/fin_gold.txt'
            file2 = 'data/fin_grc/grc_gold.txt'
            gold = 'data/fin_grc/fin_grc.gold'
            align_file(file1, file2, 'simalign-itermax', gold,layernumber)
            f1_matrix.append(str(f1))
            f1_matrix.append('/')
            prec_matrix.append(str(prec))
            prec_matrix.append('/')
            rec_matrix.append(str(rec))
            rec_matrix.append('/')
            aer_matrix.append(str(aer))
            aer_matrix.append('/')
        elif i=='fin_heb':
            file1 = 'data/fin_heb/fin_gold.txt'
            file2 = 'data/fin_heb/heb_gold.txt'
            gold = 'data/fin_heb/fin_heb.gold'
            align_file(file1, file2, 'simalign-itermax', gold,layernumber)
            f1_matrix.append(str(f1))
            f1_matrix.append('/')
            prec_matrix.append(str(prec))
            prec_matrix.append('/')
            rec_matrix.append(str(rec))
            rec_matrix.append('/')
            aer_matrix.append(str(aer))
            aer_matrix.append('/')




    f=open('f1.txt','a')
    f.writelines(f1_matrix)
    p=open('prec.txt','a')
    p.writelines(prec_matrix)
    r=open('rec.txt','a')
    r.writelines(rec_matrix)
    a=open('aer.txt','a')
    a.writelines(aer_matrix)




