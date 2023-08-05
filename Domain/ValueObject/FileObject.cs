using System.ComponentModel.DataAnnotations;

namespace AlfaCoreDumped.Domain.ValueObject
{
    public class FileObject
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public byte[] FileData { get; set; }
    }
}
