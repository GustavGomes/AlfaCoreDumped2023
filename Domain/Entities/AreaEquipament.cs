using System.ComponentModel.DataAnnotations;

namespace AlfaCoreDumped.Domain.Entities
{
    public class AreaEquipament
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public string AreaOrEquipament { get; set; }

        [Required]
        public string Code { get; set; }

        [Required]
        public string Description { get; set; }

        [Required]
        public bool LiberationStatus { get; set; }

        [Required]
        public byte[] PdfFile { get; set; }

    }
}
