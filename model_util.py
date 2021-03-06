import generate_data as gd
import numpy as np
import random
import json
import itertools
import math
import data_util as du

def sentence_to_id(sentence, word_to_id, max_len):
    ret = [word_to_id[word.lower()] for word in sentence.split()[:max_len]]
    return ret + [1] * (max_len -len(ret))

def label_to_num(l):
    d = {'entailment':0, 'contradiction':1, 'neutral':2,"equivalence":0, "independence":1, "entails":2, "reverse entails":3, "cover":4, "contradiction2":5, "alternation":6}
    return d[l]

def get_feed(path, batch_size, word_to_id, max_premise_length, max_hypothesis_length, num_iter = None, shuffle = False):
    data,_,_ = gd.process_data(1.0)
    premises = []
    premise_lengths = []
    hypotheses = []
    hypothesis_lengths = []
    labels = []
    with open(path,'r') as f:
        lines = f.readlines()
        if shuffle:
            random.shuffle(lines)
        for line in lines:
            example = json.loads(line)
            if " and " in example["sentence1"] or " or " in example["sentence1"] or " then " in example["sentence1"]:
                prem = du.parse_sentence(data,example["sentence1"])[0].emptystring + " " + du.parse_sentence(data,example["sentence1"])[1]+ " " + du.parse_sentence(data,example["sentence1"])[2].emptystring
                hyp = du.parse_sentence(data,example["sentence2"])[0].emptystring + " " + du.parse_sentence(data,example["sentence2"])[1]+ " " + du.parse_sentence(data,example["sentence2"])[2].emptystring
                premises.append(sentence_to_id(prem, word_to_id, max_premise_length))
                premise_lengths.append(len(prem.split()))
                hypotheses.append(sentence_to_id(hyp, word_to_id, max_hypothesis_length))
                hypothesis_lengths.append(len(hyp.split()))
            else:
                sentence1 = example["sentence1"]
                sentence2 = example["sentence2"]
                premises.append(sentence_to_id(sentence1, word_to_id, max_premise_length))
                premise_lengths.append(len(sentence1.split()))
                hypotheses.append(sentence_to_id(sentence2, word_to_id, max_hypothesis_length))
                hypothesis_lengths.append(len(sentence2.split()))
            labels.append(label_to_num(example["gold_label"]))
            if num_iter is not None and len(labels) > num_iter*batch_size:
                break
    if num_iter is None:
        num_iter = int(math.ceil(len(labels)/ batch_size))
    for i in range(num_iter):
        yield (np.array(premises[i * batch_size: (i+1) * batch_size]),
               np.array(premise_lengths[i * batch_size: (i+1) * batch_size]),
               np.array(hypotheses[i * batch_size: (i+1) * batch_size]),
               np.array(hypothesis_lengths[i * batch_size: (i+1) * batch_size]),
               np.array(labels[i * batch_size: (i+1) * batch_size]),
               9)

def crazy2_get_feed(path, batch_size, word_to_id, max_premise_length, max_hypothesis_length, num_iter = None, shuffle = False):
    data,_,_ = gd.process_data(1.0)
    premises = []
    premise_lengths = []
    hypotheses = []
    hypothesis_lengths = []
    labels = []
    with open(path+"1256",'r') as f:
        lines = f.readlines()
        if shuffle:
            random.shuffle(lines)
        for line in lines:
            example = json.loads(line)
            if " and " in example["sentence1"] or " or " in example["sentence1"] or " then " in example["sentence1"]:
                prem = du.parse_sentence(data,example["sentence1"])[0].emptystring + " " + du.parse_sentence(data,example["sentence1"])[1]+ " " + du.parse_sentence(data,example["sentence1"])[2].emptystring
                hyp = du.parse_sentence(data,example["sentence2"])[0].emptystring + " " + du.parse_sentence(data,example["sentence2"])[1]+ " " + du.parse_sentence(data,example["sentence2"])[2].emptystring
                premises.append(sentence_to_id(prem, word_to_id, max_premise_length))
                premise_lengths.append(len(prem.split()))
                hypotheses.append(sentence_to_id(hyp, word_to_id, max_hypothesis_length))
                hypothesis_lengths.append(len(hyp.split()))
            else:
                sentence1 = example["sentence1"]
                sentence2 = example["sentence2"]
                premises.append(sentence_to_id(sentence1, word_to_id, max_premise_length))
                premise_lengths.append(len(sentence1.split()))
                hypotheses.append(sentence_to_id(sentence2, word_to_id, max_hypothesis_length))
                hypothesis_lengths.append(len(sentence2.split()))
            labels.append([label_to_num(example["gold_label"][i]) for i in range(12)])
            if num_iter is not None and len(labels) > num_iter*batch_size:
                break
    if num_iter is None:
        num_iter = int(math.ceil(len(labels)/ batch_size))
    for i in range(num_iter):
        yield (np.array(premises[i * batch_size: (i+1) * batch_size]),
               np.array(premise_lengths[i * batch_size: (i+1) * batch_size]),
               np.array(hypotheses[i * batch_size: (i+1) * batch_size]),
               np.array(hypothesis_lengths[i * batch_size: (i+1) * batch_size]),
               np.array(labels[i * batch_size: (i+1) * batch_size]),
               1256)

def crazy_get_feed(path, batch_size, word_to_id, max_premise_length, max_hypothesis_length, num_iter = None, shuffle = False):
    data,_,_ = gd.process_data(1.0)
    premises = [[], [], [], [], []]
    premise_lengths = [[], [], [], [], []]
    hypotheses = [[], [], [], [], []]
    hypothesis_lengths = [[], [], [], [], []]
    labels = [[], [], [], [], []]
    for i, type in enumerate(["", "1", "2", "5", "6"]):
        with open(path+type,'r') as f:
            lines = f.readlines()
            if shuffle:
                random.shuffle(lines)
            for line in lines:
                example = json.loads(line)
                if " and " in example["sentence1"] or " or " in example["sentence1"] or " then " in example["sentence1"]:
                    prem = du.parse_sentence(data,example["sentence1"])[0].emptystring + " " + du.parse_sentence(data,example["sentence1"])[1]+ " " + du.parse_sentence(data,example["sentence1"])[2].emptystring
                    hyp = du.parse_sentence(data,example["sentence2"])[0].emptystring + " " + du.parse_sentence(data,example["sentence2"])[1]+ " " + du.parse_sentence(data,example["sentence2"])[2].emptystring
                    premises.append(sentence_to_id(prem, word_to_id, max_premise_length))
                    premise_lengths.append(len(prem.split()))
                    hypotheses.append(sentence_to_id(hyp, word_to_id, max_hypothesis_length))
                    hypothesis_lengths.append(len(hyp.split()))
                else:
                    sentence1 = example["sentence1"]
                    sentence2 = example["sentence2"]
                    premises[i].append(sentence_to_id(sentence1, word_to_id, max_premise_length))
                    premise_lengths[i].append(len(sentence1.split()))
                    hypotheses[i].append(sentence_to_id(sentence2, word_to_id, max_hypothesis_length))
                    hypothesis_lengths[i].append(len(sentence2.split()))
                labels[i].append(label_to_num(example["gold_label"]))
                if num_iter is not None and len(labels) > num_iter*batch_size:
                    break
    if num_iter is None:
        num_iter = int(math.ceil(len(labels[0])/ batch_size))
    batches = []
    for i in range(num_iter):
        for j in range(5):
            batches.append((i,j))
    lengths = {0:9, 1:1, 2:2, 3:5, 4:6}
    random.shuffle(batches)
    random.shuffle(batches)
    random.shuffle(batches)
    for i,j in batches:
        yield (np.array(premises[j%5][i * batch_size: (i+1) * batch_size]),
               np.array(premise_lengths[j%5][i * batch_size: (i+1) * batch_size]),
               np.array(hypotheses[j%5][i * batch_size: (i+1) * batch_size]),
               np.array(hypothesis_lengths[j%5][i * batch_size: (i+1) * batch_size]),
               np.array(labels[j%5][i * batch_size: (i+1) * batch_size]),
               lengths[j])

def get_vocab():
    data, _, _ = gd.process_data(1.0)
    vocab = ["doesnot", "any", "or", "and", "if", "then", "emptystring", "notevery"]
    for k in data:
        for word in data[k]:
            if type(word) == list:
                vocab += [w.lower() for w in word]
            else:
                vocab.append(word.lower())
    return vocab

def get_word_to_id(vocab):
    word_to_id = dict()
    for i, word in enumerate(vocab):
        word_to_id[word] = i
    return word_to_id

def get_id_to_word(glovepath, vocab):
    d = _get_word_to_id(glovepath, vocab)
    result = {}
    for word in d:
        result[d[word]] = word
    return result

def get_word_vec(vocab, dimension):
    mat = []
    for word in vocab:
        mat.append([random.uniform(-1,1) for _ in range(dimension)])
    return np.array(mat, dtype=np.float32)
