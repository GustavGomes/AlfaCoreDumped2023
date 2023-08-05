using System.ComponentModel.DataAnnotations;

namespace AlfaCoreDumped.Domain.Entities
{
    public class Report
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public string ReporterName { get; set; }

        [Required]
        public string CostCenter { get; set; }

        [Required]
        public string Description { get; set; }

        [Required]
        public string OperationField { get; set; }

        [Required]
        public DateTime Created { get; set; }

        public ICollection<byte[]> Pictures { get; set; }
    }
}
