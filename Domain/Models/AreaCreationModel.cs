using System.ComponentModel.DataAnnotations;

namespace AlfaCoreDumped.Domain.Models
{
    public class AreaCreationModel
    {

        [Required]
        public string Code { get; set; }

        [Required]
        public string Description { get; set; }

        [Required]
        public bool LiberationStatus { get; set; }

        public byte[] PdfFile { get; set; }
    }
}
