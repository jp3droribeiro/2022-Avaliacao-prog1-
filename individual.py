
class Individual:
    
    n = 0
    def __init__(self,genotype,name=None):
        if name == None:
            Individual.n += 1
            name = 'Indiv'+str(Individual.n)

        self._name=name
        self._genotype=genotype
        self._list_genotypes=['AA','Ai','BB','Bi','AB','ii']
        
        if genotype not in self._list_genotypes:
            raise ValueError(f'Invalid genotype try:{self._list_genotypes}')

    def __str__(self):
        return (("%s,%s")%(self.name,self.genotype))

    @property
    def name(self):
        return self._name 
    @property
    def genotype(self):
        return self._genotype
    @property    
    def blood_type(self):
        if self.genotype == 'AA'or self.genotype == 'Ai':
            return 'A'
        if self.genotype == 'BB'or self.genotype == 'Bi':
            return 'B'
        if self.genotype == 'AB':
            return 'AB'
        if self.genotype == 'ii':
            return 'O'
    @property
    def agglutinogens(self):
        if self.blood_type == 'A':
            return 'A'
        if self.blood_type == 'B':
            return 'B'
        if self.blood_type == 'AB':
            return 'A','B'
        if self.blood_type == 'O':
            return 'no agglutinogens.'
    @property
    def agglutinins(self):
        if self.blood_type == 'A':
            return 'B'
        if self.blood_type == 'B':
            return 'A'
        if self.blood_type == 'AB':
            return  'No agglutinins'
        if self.blood_type == 'O':
            return  'A','B'

    def offsprings_genotypes(self,indiv2): 
        list_genotypes = []
        for allele1 in self.genotype:
            for allele2 in indiv2.genotype:
                list_genotypes.append(allele1 + allele2)
        list_genotypes = list(set(list_genotypes))            
        return list_genotypes

    def offsprings_blood_types(self,indiv2):
        bloodtype_list=[]
        for g in self.offsprings_genotypes(indiv2):
            if g =='AA' in self.offsprings_genotypes(indiv2) or g == 'Ai' in self.offsprings_genotypes(indiv2):
                bloodtype_list.append('A') 
            if g =='BB' in self.offsprings_genotypes(indiv2) or g == 'Bi' in self.offsprings_genotypes(indiv2):
                bloodtype_list.append('B')
            if g == 'AB' in self.offsprings_genotypes(indiv2):
                bloodtype_list.append('AB')
            if g == 'ii'in self.offsprings_genotypes(indiv2):
                bloodtype_list.append('O')
        return bloodtype_list
 
    def can_donate(self,indiv2):
        if self.blood_type == indiv2.blood_type:
            return True
        elif self.blood_type == 'O' and indiv2.blood_type == 'A':
            return True
        elif self.blood_type == 'O' and indiv2.blood_type == 'B':
            return True
        elif self.blood_type == 'O' and indiv2.blood_type == 'AB':
            return True
        elif self.blood_type == 'A' and indiv2.blood_type == 'AB': 
            return True
        elif self.blood_type == 'B' and indiv2.blood_type == 'AB':
            return True
        else:
            return False
    
    def can_receive(self,indiv2):
        if self.blood_type == indiv2.blood_type:
            return True
        elif self.blood_type == 'AB' and indiv2.blood_type == 'O':
            return True
        elif self.blood_type == 'AB' and indiv2.blood_type == 'A':
            return True
        elif self.blood_type == 'AB' and indiv2.blood_type == 'B':
            return True
        elif self.blood_type == 'A' and indiv2.blood_type == 'O':
            return True
        elif self.blood_type == 'B' and indiv2.blood_type == 'O':
            return True
        else:
            return False  

    
