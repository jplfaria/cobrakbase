from modelseedpy.core.mstemplate import MSTemplateBiomass, MSTemplateBiomassComponent

class NewModelTemplateBiomass(MSTemplateBiomass):
    def __init__(
        self,
        bio_id,
        name,
        type,
        dna,
        rna,
        protein,
        lipid,
        cellwall,
        cofactor,
        pigment,
        carbohydrate,
        energy,
        other
    ):
        super().__init__(
            bio_id,
            name,
            type,
            dna,
            rna,
            protein,
            lipid,
            cellwall,
            cofactor,
            pigment,
            carbohydrate,
            energy,
            other
        )

    @staticmethod
    def from_dict(d, template):
        self = NewModelTemplateBiomass(
            d["id"],
            d["name"],
            d["type"],
            d["dna"],
            d["rna"],
            d["protein"],
            d["lipid"],
            d["cellwall"],
            d["cofactor"],
            d.get("pigment", 0), #this change is necessary for instances where category "pigment" is not present
            d.get("carbohydrate", 0), #this change is necessary for instances where category "carbohydrate" is not present
            d["energy"],
            d["other"],
        )
        for item in d["templateBiomassComponents"]:
            biocomp = MSTemplateBiomassComponent.from_dict(item, template)
            self.templateBiomassComponents.add(biocomp)
        self._template = template
        return self